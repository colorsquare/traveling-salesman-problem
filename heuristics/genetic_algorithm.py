"""
Genetic Algorithm (GA)

Heuristic approach imitating biological evolution in nature.
"""


def insertion_sort(generation, elem):
    """Insert a new element to a generation.

    Args:
        generation (list[tuple]): List of elements `elem` below.
            Sorted in order of distance, elem[1].
        elem (tuple[list[int], int]): A tuple of route and its distance of class TSP.

    Returns:
        generation (list[tuple]): List with `elem` inserted.
    """
    route, total_distance = elem

    insert_pos = 0
    while insert_pos < len(generation) and total_distance > generation[insert_pos][1]:
        insert_pos += 1
    generation.insert(insert_pos, (route, total_distance))

    return generation


def genetic_algorithm(tsp):
    """Traveling salesman problem (TSP) solved with genetic algorithm.

    Args:
        tsp (class `TSP`): An instance of traveling salesman problem (TSP)

    Updates:
        tsp.route (list[int]): Heuristically optimized route with minimal cost of travel distances.
        tsp.total_distance (int): Total distance calculated with tsp.route.
    """

    def create_first_generation(population):
        first_generation = []

        for _ in range(population):
            new_route = tsp.create_random_route()
            new_total_distance = tsp.calculate_total_distance(new_route)
            insertion_sort(first_generation, (new_route, new_total_distance))

        return first_generation

    def create_child_generation(parent_generation):
        # TODO
        population = len(parent_generation)
        n = population // 2
        return sorted(
            parent_generation[:n] + create_first_generation(population - n),
            key=lambda e: e[1],
        )

    population = len(tsp.distances)
    parent_generation = create_first_generation(population)

    no_evolution_count = 0
    while no_evolution_count < 3:
        child_generation = create_child_generation(parent_generation)
        print(child_generation)
        no_evolution_count = (
            0
            if child_generation[0][1] < parent_generation[0][1]
            else no_evolution_count + 1
        )
        parent_generation = child_generation

    tsp.update_route(child_generation[0][0], child_generation[0][1])
