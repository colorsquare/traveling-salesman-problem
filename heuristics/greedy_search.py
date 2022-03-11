import time
from helper import *


def greedy_search(tsp):
    """Local search algorithm with the idea of 'making best choices every step',
    by choosing the nearest city among non-visited.

    Args:
        tsp (object TSP): tsp with random representation.
    """
    start_time = time.time()  # starting time

    visited = tsp.representation[:1]  # random start city from representation
    current = visited[-1]
    while len(visited) != len(tsp.coordinates):  # until representation is full
        next_cities = sorted(
            [
                (distance, idx)
                for idx, distance in enumerate(tsp.distances[current])
                if idx not in visited  # only those not already visited
            ]
        )
        next_city = next_cities[0][1]  # get the nearest city
        visited.append(next_city)
        current = next_city
    tsp.representation = visited + visited[:1]

    print("Reached local optimum")
    show_time_fitness(start_time, tsp)
    return tsp


if __name__ == "__main__":
    # gives error if imported on top
    from main import load

    data = parse()
    tsp = load(data)

    # TODO: for more various experiments especially with greedy_search.py
    greedy_search(tsp)
