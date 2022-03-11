import time
from helper import *


def compare_switch(tsp, start, end):
    """Compare current and switched distances,
    and perform switch if latter is shorter.

    Args:
        tsp (object TSP): tsp with random representation.
        start (Integer): starting point (included) of switch
        end (Interger): ending point (excluded) of switch

    Returns:
        switched (Bool): True if switched, False otherwise.

    Examples:
        Assume representation: [3, 1, 4, 2, 5, 0, 3]
        start: 2, end: 5 -> start ~ end: [4, 2, 5]
    """
    # make abbrs for readability
    r = tsp.representation
    d = tsp.distances

    current_distance = d[r[start - 1]][r[start]] + d[r[end - 1]][r[end]]
    swapped_distance = d[r[start - 1]][r[end - 1]] + d[r[start]][r[end]]

    if swapped_distance < current_distance:
        tsp.representation = r[:start] + r[start:end][::-1] + r[end:]
        return True
    return False


def two_opt(tsp):
    """Local search algorithm with an idea of 'untying',
    by simply swapping two roads.

    Args:
        tsp (object TSP): tsp with random representation.
    """
    start_time = time.time()  # starting time
    n = len(tsp.coordinates)  # number of cities

    optimal = False
    while not optimal:
        modified = False
        for start in range(1, n - 1):
            for end in range(start + 2, n + 1):
                if compare_switch(tsp, start, end):
                    # show_time_fitness(start_time, tsp)
                    modified = True
                    break
            if modified:
                break
        if not modified:
            print("Reached local optimum")
            show_time_fitness(start_time, tsp)
            optimal = True


if __name__ == "__main__":
    # gives error if imported on top
    from main import load

    data = parse()
    tsp = load(data)

    # TODO: for more various experiments especially with two_opt.py
    two_opt(tsp)
