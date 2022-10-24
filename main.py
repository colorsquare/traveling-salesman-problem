"""
Entry point of execution.
With desired solver and data, run and save the solution.

To run this file,
$ python3 main.py [method] [data]
"""
import time
import argparse

from tsp import TSP
from heuristics.genetic_algorithm import genetic_algorithm
from heuristics.greedy_search import greedy_search
from heuristics.two_opt import two_opt

METHODS = {
    "ga": genetic_algorithm,
    "greedy": greedy_search,
    "2opt": two_opt,
}


def main():
    """Parse, build problem instance, execute, and save the solution.

    Raises:
        ValueError: If method is not found.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "method",
        nargs="?",  # number of arguments, ? is 0 or 1 in regex.
        default="ga",
        help="Use abbreviations for methods. { 'ga': genetic-algorithm, 'greedy': greedy-search, '2opt': 2-opt }",
    )
    parser.add_argument(
        "data",
        nargs="?",
        default="a280",
        help="Name of '*.tsp' files. ex. bier127, a280, vm1748, ..",
    )
    args = parser.parse_args()
    method, data = args.method, args.data

    time.sleep(0.3)
    print(
        "Running with { method: '%s', data: '%s' }. \nInitializing TSP instance.."  # pylint: disable=consider-using-f-string
        % (method, data)
    )

    tsp = TSP(data)
    time.sleep(0.3)
    solver = METHODS.get(method)
    if solver is None:
        raise ValueError(
            "Method not found. Run below command for details.\n  $ python3 main.py --help"
        )

    print(f"Solving '{data}.tsp' with '{solver.__name__}'..")
    time.sleep(0.3)

    solver(tsp)
    best_route, best_distance = tsp.route, tsp.total_distance
    s = "\n".join([str(city_index + 1) for city_index in best_route])
    with open("solution.csv", "w", encoding="utf-8") as f:
        f.write(s)

    print(f"\nShortest distance found: {best_distance}\nRoute saved to 'solution.csv'.")


if __name__ == "__main__":
    main()
