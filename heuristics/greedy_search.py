"""
Greedy Search

Baseline approach, greedily searching for the best answer.

However, our problem instance has numerous local optima.
Therefore, this approach does not guarantee the global optimum.
"""


def greedy_search(tsp):
    """Traveling salesman problem (TSP) solved with greedy search.

    Args:
        tsp (class `TSP`): An instance of traveling salesman problem (TSP)

    Updates:
        tsp.route (list[int]): Heuristically optimized route with minimal cost of travel distances.
        tsp.total_distance (int): Total distance calculated with tsp.route.
    """
    route = [tsp.route[0]]  # random starting point
    unvisited = [city for city in list(range(len(tsp.locations))) if city != route[0]]

    while len(route) < len(tsp.locations):
        nearest, nearest_dist = None, None
        for city in unvisited:
            distance = tsp.distances[max(route[-1], city)][min(route[-1], city)]
            if not nearest_dist or distance < nearest_dist:
                nearest_dist = distance
                nearest = city
        route.append(nearest)
        unvisited.remove(nearest)

    tsp.route = route
    tsp.total_distance = tsp.calculate_total_distance(route)
