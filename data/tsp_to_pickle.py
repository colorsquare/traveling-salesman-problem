import argparse
import pickle
import math


# list of mp-testdata available.
# TODO: change on modifying mp-dataset.
_FILES = ["a280", "bier127", "burma14", "pr76", "rl11849", "test", "u2152", "vm1748"]


def parse():
    """Parse command line arguments using `argparse`.

    Returns:
        file (String): File name.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Name of tsp file to transform")

    args = parser.parse_args()
    return args.file


def read(file):
    """Read .tsp file, and build TSP coordinates, distances list.

    Args:
        file (String): File name.

    Returns:
        coordinates (List): Location of cities. Each city's x, y coordinates are expressed as tuples.
        distances (List): Pre-calculated distances between all cities. n x n matrix.

    Raises:
        FileNotFoundError: If `file` is not found in `_FILES`.
    """
    # check if `file` is valid.
    if file not in _FILES:
        raise FileNotFoundError(
            """Invalid file -> '%s'
            Please refer to .tsp files in `mp-dataset`.
            (ex) a280, bier127, burma14, .."""
            % file
        )

    # open desired mp_dataset
    f = open("mp-testdata/" + file + ".tsp", encoding="utf-8")

    # read until reaches "NODE_COORD_SECTION\n"
    while f.readline() != "NODE_COORD_SECTION\n":
        pass

    # build coordinates
    coordinates = []
    line = f.readline().strip()
    while line != "EOF":  # breaks when reaches the End Of File
        coordinate = line.split()[-2:]
        coordinates.append(
            (float(coordinate[0]), float(coordinate[1]))
        )  # save as tuple of floats
        line = f.readline().strip()  # new line
    f.close()

    # build distances
    n = len(coordinates)  # n x n matrix
    distances = [
        [
            math.hypot(
                coordinates[i][0] - coordinates[j][0],  # diff of x coordinate
                coordinates[i][1] - coordinates[j][1],  # diff of y coordinate
            )
            for j in range(n)
        ]
        for i in range(n)
    ]

    return coordinates, distances


def save(file, coordinates, distances):
    """Save coordinates, distances in a separate .pickle file.

    Args:
        file (String): File name.
        coordinates (List): Location of cities. Each city's x, y coordinates are expressed as tuples.
        distances (List): Pre-calculated distances between all cities. n x n matrix.
    """
    # Pickle the 'data' dictionary using the highest protocol available.
    with open(file + "_coordinates.pickle", "wb") as f:
        pickle.dump(coordinates, f, pickle.HIGHEST_PROTOCOL)

    with open(file + "_distances.pickle", "wb") as f:
        pickle.dump(distances, f, pickle.HIGHEST_PROTOCOL)


def main():
    """Transforms each element `mp-testdata` from .tsp to .pickle files."""
    # parse cli file name
    file = parse()
    # read file into coordinates, distances
    coordinates, distances = read(file)
    # save as .pickle files
    save(file, coordinates, distances)


if __name__ == "__main__":
    main()
