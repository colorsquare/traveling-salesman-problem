"""
Two Opt (2-opt)

Unties any 'X' crossroads, until there are none.

A     D         A ---- D
  \ /
  / \      =>
B     C         B ---- C

Exhaustively loop through all possible ties. (nC2)
However, this approach also does not guarantee the global optima.
"""


def two_opt(tsp):
    """Traveling salesman problem (TSP) solved with 2-opt.

    Args:
        tsp (class `TSP`): An instance of traveling salesman problem (TSP)

    Updates:
        tsp.route (list[int]): Heuristically optimized route with minimal cost of travel distances.
        tsp.total_distance (int): Total distance calculated with tsp.route.
    """
    route = tsp.route

    modified = True
    while modified:
        modified = False
        for i, _ in enumerate(route):
            for j, _ in enumerate(route[i + 1 :]):
                j = i + j
                # i - 1 is -1, the last index,
                # when i points to the first element.
                ll, lr = route[i - 1], route[i]
                rl, rr = route[j], route[(j + 1) % len(route)]
                if (
                    tsp.distances[max(ll, rl)][min(ll, rl)]
                    + tsp.distances[max(lr, rr)][min(lr, rr)]
                ) < (
                    tsp.distances[max(ll, lr)][min(ll, lr)]
                    + tsp.distances[max(rl, rr)][min(rl, rr)]
                ):
                    modified = True
                    route[i : j + 1] = route[i : j + 1][::-1]

    tsp.route = route
    tsp.total_distance = tsp.calculate_total_distance(route)
