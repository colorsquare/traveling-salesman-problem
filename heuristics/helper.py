import argparse
import time


def parse():
    """Parse command line arguments using `argparse`.

    Returns:
        file (String): File name.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Data file to solve")

    args = parser.parse_args()
    return args.file


def show_time_fitness(start_time, tsp):
    """Show elapsed time, and tsp fitness.

    Args:
        start_time (Timestamp): starting time from time.time()
        tsp (object TSP)
    """
    print("Time elapsed: %f" % (time.time() - start_time))
    print("Fitness: %f" % tsp.get_fitness())
