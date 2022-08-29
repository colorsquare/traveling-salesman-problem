"""
Genetic Algorithm (GA)

Heuristic approach imitating biological evolution in nature.

Before we begin, to not lose the best performing routes, we keep the top 10% or at least
one parent, that presents shortest distance. It's called 'elitism'.

For the rest, the probabilites for each operations shows the likelihood to be selected
when creating a child. Exploitation takes 90%, mutation 10%.

On exploitation, we propose untie (remove 'X' crossroads), point switch (resolve zigzag),
greedy point (relocate to nearest).
(Point switch is a part of 'untie', but added to focus on resolving zigzags)

A     D         A ---- D
  \ /
  / \      =>
B     C         B ---- C

A     D         A ---- D
|   / |              /
|  /  |    =>      /
| /   |           /
B     C         B ---- C

A              D        A ------------ D
| \          / |        |              |
|   \       |  |        |              |
|     \     |  |        |              |
|       \  /   |   =>   |              |
|         E    |        |          E   |
|              |        |        /   \ |
B ------------ C        B ------       C

On mutation, we propose random switch (exchange random two cities), and greedy sublist
(reorder cluster, 'E' above can be a cluster).
"""

import random


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

    def create_first_generation():
        first_generation = []

        population = max(3, len(tsp.distances) // 10)
        for _ in range(population):
            new_route = tsp.create_random_route()
            new_total_distance = tsp.calculate_total_distance(new_route)
            insertion_sort(first_generation, (new_route, new_total_distance))

        return first_generation

    def create_child_generation(parent_generation):
        """Create next generation with genetic operations.

        Args:
            parent_generation (list[tuple[list[int], int]]): List of tuple elements,
                (route, total_distance) of class TSP.

        Returns:
            child_generation (list[tuple[list[int], int]]): Next generation built,
                with genetic operations (elitism, crossover, mutation, and random).
        """

        def choose_parent():
            n = max(1, int(len(parent_generation) * 0.2))
            rand = random.random()
            return random.choice(
                parent_generation[:n] if rand < 0.8 else parent_generation[n:]
            )[0]

        def crossover():
            parent1 = choose_parent()
            parent2 = choose_parent()
            i, j = random.randrange(len(parent1)), random.randrange(len(parent1))
            # slice random presentation from a parent,
            # and fill the rest with the order of another parent
            child1 = parent1[min(i, j) : max(i, j) + 1]
            child2 = [gene for gene in parent2 if gene not in child1]
            return child1 + child2

        def point_mutation():
            child = choose_parent()
            point = random.randrange(len(child))
            if point == len(child) - 1:
                child[0], child[-1] = child[-1], child[0]
            else:
                child[point], child[point + 1] = child[point + 1], child[point]
            return child

        def random_mutation():
            child = choose_parent()
            i, j = random.randrange(len(child)), random.randrange(len(child))
            child[i], child[j] = child[j], child[i]
            return child

        def permute_mutation():
            child = choose_parent()
            i, j = random.randrange(len(child)), random.randrange(len(child))
            i, j = min(i, j), max(i, j) + 1
            permutation = child[i:j]
            random.shuffle(permutation)
            child[i:j] = permutation
            return child

        population = len(parent_generation)
        number_of_children = max(1, population // 10)
        child_generation = parent_generation[:number_of_children]

        while len(child_generation) < population:
            rand = random.random()
            if rand < 0.6:
                child = crossover()
            elif rand < 0.7:
                child = point_mutation()
            elif rand < 0.8:
                child = random_mutation()
            elif rand < 0.9:
                child = permute_mutation()
            else:
                child = tsp.create_random_route()

            insertion_sort(
                child_generation, (child, tsp.calculate_total_distance(child))
            )
            number_of_children += 1

        return child_generation

    parent_generation = create_first_generation()

    no_evolution_count = 0
    while no_evolution_count < max(3, len(parent_generation) // 10):
        child_generation = create_child_generation(parent_generation)
        no_evolution_count = (
            0
            if child_generation[0][1] < parent_generation[0][1]
            else no_evolution_count + 1
        )
        parent_generation = child_generation

    tsp.update_route(child_generation[0][0], child_generation[0][1])
