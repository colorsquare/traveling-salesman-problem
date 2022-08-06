class TSP:
    """An instance of traveling salesman problem (TSP).

    Note:
        Number of cities in an instance is `n`.
        Cities do not have names. Instead, they are referred by indexes in a list.

    Attributes:
        locations (list[tuple[int]]): Each city location is represented as a tuple[int],
            an euclidien coordinate (x, y).
        distances (list[list[int]]): Pre-calculated distances between all cities. n x n matrix.
        representation (list[int]): List of cities, in order of salesman's travel.
    """

    def __init__(self):
        self.coordinates = []
