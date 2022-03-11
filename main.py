import argparse
import pickle
from tsp import TSP

# method modules
from heuristics.greedy_search import greedy_search
from heuristics.two_opt import two_opt
from heuristics.genetic_programming import genetic_programming


# TODO: change comments in parse(), get_solver() below, if new method is added.
_METHODS = {
    "greedy": greedy_search,
    "2opt": two_opt,
    "gp": genetic_programming,
}


def parse():
    """Parse command line arguments using `argparse`.

    Returns:
        args (object Namespace): Contains each argument by attribute.

    Examples:
        >>> args = parser.parse_args()  # from `return` line
        >>> args.method, args.data
        'gp', 'rl11849'
    """
    parser = argparse.ArgumentParser(
        description="Executes solver 'method' with 'data'. Default arguments are 'gp', 'rl11849'"
    )
    parser.add_argument(
        "method",
        nargs="?",
        default="gp",
        help="""The abbreviation for the methods are:
                { greedy: greedy-search, 2opt: 2-opt, gp: genetic-programming }""",
    )  # nargs: number of args / '?' : regex of 0 or 1.
    parser.add_argument(
        "data",
        nargs="?",
        default="rl11849",
        help="""Refer to .tsp files in 'mp-dataset'.
                (ex) a280, bier127, burma14, ..""",
    )

    # return args in object Namespace
    return parser.parse_args()


def get_solver(method):
    """Matches `method` to solver functions.

    Args:
        method (String): Abbreviation for each method.
            Refer to attribute `help` of the line `parser.add_argument('method', ...)` from function `parse`.

    Returns:
        solver_function (Function): Each function is imported from solver modules.

    Raises:
        ValueError: If `method` is not found in `_METHODS`.
    """
    solver_function = _METHODS.get(method, None)
    if not solver_function:
        raise ValueError(
            """Invalid method -> '%s'
            The abbreviation for the methods are:
            { greedy: greedy-search, 2opt: 2-opt, gp: genetic-programming }"""
            % method
        )
    return solver_function


def load(data):
    """Load coordinates, distances as a TSP instance.

    Args:
        data (String): Data name.

    Returns:
        tsp (object TSP): Initialized tsp.

    Exits:
        When '.pickle' files for `data` is not found.
    """
    try:
        with open("data/" + data + "_coordinates.pickle", "rb") as f:
            coordinates = pickle.load(f)

        with open("data/" + data + "_distances.pickle", "rb") as f:
            distances = pickle.load(f)

    except FileNotFoundError:
        print(
            "\n"
            "'.pickle' files of '%s' does not exist.\n"
            "Please refer to README.md on how to create .pickle files." % data
        )
        exit(0)

    # create a TSP instance
    tsp = TSP(coordinates, distances)
    return tsp


def main():
    """Main entry point of execution.

    Parse arguments, show them, and run solver.
    """
    args = parse()

    solver = get_solver(args.method)  # solver function
    tsp = load(args.data)  # instance of class TSP

    # running with..
    print(
        "\nSolving traveling salesman problem '%s' with method '%s'.."
        % (args.data, solver.__name__)
    )

    # starting fitness
    print("Starting fitness: %f\n" % tsp.get_fitness())
    solver(tsp)  # run heuristic approach


# 'if' statement determines if this file is the 'start'.
# main() is only executed if this file is used as beginning of execution. If else, used as module, this is not executed.
if __name__ == "__main__":
    main()
