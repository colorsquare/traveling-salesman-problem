"""
Traveling Salesman Problem (TSP)

Built into python class with some helper functions.

To run doctests,
$ python3 -m doctest -v tsp.py
"""
import math
import random


class TSP:
    """An instance of traveling salesman problem (TSP).

    Note:
        Number of cities in an instance is `n`.
        Cities do not have names. Instead, they are referred by indexes in a list.

    Attributes:
        locations (list[tuple[int]]): Each city location is represented as a tuple[int],
            an euclidien coordinate (x, y).
        distances (list[list[int]]): Pre-calculated distances between all cities.
            n x n matrix cut in half, a bottom-left triangle.
        route (list[int]): List of cities, in order of the salesman's travel.
        total_distance (int): Cumulative distance of the route.
    """

    def __init__(self, data):
        self.locations = self._build_locations(data)
        self.distances = self._build_distances()

        self.route = self.create_random_route()
        self.total_distance = self.calculate_total_distance(self.route)

    def _build_locations(self, data):
        """Read data and build attribute 'locations'.

        Args:
            data (str): Name of a '.tsp' file.

        Returns:
            locations (list[tuple[int]])

        Raises:
            FileNotFoundError: if argument 'data' is not found in 'data/' folder.
        """
        locations = []
        with open(f"data/{data}.tsp", encoding="utf-8") as file:
            while file.readline() != "NODE_COORD_SECTION\n":
                pass
            line = file.readline().strip()
            while line != "EOF":  # End Of File
                location = line.split()[-2:]
                locations.append((float(location[0]), float(location[1])))
                line = file.readline().strip()

        return locations

    def _build_distances(self):
        """Build attribute 'distances'.

        Returns:
            distances (list[list[int]])
        """
        distances = [
            [
                math.hypot(
                    self.locations[i][0] - self.locations[j][0],
                    self.locations[i][1] - self.locations[j][1],
                )
                for j in range(i)
            ]
            for i in range(len(self.locations))
        ]

        return distances

    def create_random_route(self):
        """Create a random route.

        Returns:
            route (list[int])
        """
        route = list(range(len(self.locations)))
        random.shuffle(route)
        return route

    def update_route(self, new_route):
        self.route = new_route
        self.total_distance = self.calculate_total_distance(self.route)

    def calculate_total_distance(self, route):
        """Add all distances that salesman will travel.

        Attribute 'distances' was cut in half since a distance between two cities are equal
        both ways. max(), min() is used to adjust index input, due to the halved n x n matrix.

        Args:
            route (list[int]): Description equal to self.route
        """
        total_distance = 0

        prev_city = route[0]
        for city in route[1:]:
            total_distance += self.distances[max(city, prev_city)][min(city, prev_city)]
            prev_city = city

        first, last = route[0], route[-1]
        total_distance += self.distances[max(first, last)][min(first, last)]

        return total_distance


# Tests


def test_tsp(data):
    """
    Examples:
        >>> test_tsp('test')
        [(0.0, 0.0), (0.0, 4.0), (3.0, 0.0), (3.0, 4.0)]
        [[], [4.0], [3.0, 5.0], [5.0, 3.0, 4.0]]
    """
    tsp = TSP(data)
    print(tsp.locations)
    print(tsp.distances)
