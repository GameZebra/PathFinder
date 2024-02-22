class GridGraph:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.obstacles = []

    def in_bounds(self, node):
        (x, y) = node
        return 0 <= x < self.rows and 0 <= y < self.cols

    def passable(self, node):
        return node not in self.obstacles

    def get_neighbors(self, node):
        (row, col) = node
        results = [(row + 1, col), (row, col - 1), (row - 1, col), (row, col + 1)]
        results = list(filter(self.in_bounds, results))
        results = list(filter(self.passable, results))
        return results
