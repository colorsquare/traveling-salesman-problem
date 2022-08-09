"""
Traveling Salesman Problem (TSP)

Built into python class with some helper functions.
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
            n x n matrix cut in half.
        route (list[int]): List of cities, in order of the salesman's travel.
        total_distance (int): Cumulative distance of the route.
    """

    def __init__(self, data):
        self._locations = self._build_locations(data)
        self._distances = self._build_distances()

        self.route = self.create_random_route()
        self.total_distance = self.calculate_total_distance()

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
                    self._locations[i][0] - self._locations[j][0],
                    self._locations[i][1] - self._locations[j][1],
                )
                for j in range(i)
            ]
            for i in range(len(self._locations))
        ]

        return distances

    def create_random_route(self):
        """Create a random route.

        Returns:
            route (list[int])
        """
        return random.shuffle(list(range(len(self._locations))))

    def update_route(self, new_route):
        self.route = new_route
        self.total_distance = self.calculate_total_distance()

    def calculate_total_distance(self):
        total_distance = 0

        prev_city = self.route[0]
        for city in self.route[1:]:
            total_distance += self._distances[max(city, prev_city)][
                min(city, prev_city)
            ]
            prev_city = city

        first, last = self.route[0], self.route[-1]
        total_distance += self._distances[max(first, last)][min(first, last)]

        return total_distance
