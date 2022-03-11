import random


class TSP:
    """Instance for traveling salesman problem.

    It includes total n cities, with euclidien coordinates x, y for each.

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        coordinates (List): Location of cities. Each city's x, y coordinates are expressed as tuples.
        distances (List): Pre-calculated distances between all cities. n x n matrix.

    Attributes:
        representation (List): Traveling sequence of cities. n + 1 in length.
        coordinates (List): Location of cities. Each city's x, y coordinates are expressed as tuples.
        distances (List): Pre-calculated distances between all cities. n x n matrix.
    """

    def __init__(self, coordinates, distances):
        self.coordinates = coordinates
        self.distances = distances
        self.representation = self._random_representation()  # random initialization

    def _random_representation(self):
        """Creates random representation, sequence of cities.

        Two starting points are fixed, but it can express all representations.
        """
        n = len(self.coordinates)
        representation = random.sample(range(n), n)
        return representation + representation[:1]  # end at where you began

    def get_fitness(self):
        """Total distance traveled by salesman, from current `representation`.

        Returns:
            total_distance (Float): sum of distances of traveling.
        """
        total_distance = 0
        prev_city = self.representation[0]
        for city in self.representation[1:]:
            total_distance += self.distances[prev_city][city]
            prev_city = city
        return total_distance
