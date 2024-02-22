from grid_graph import GridGraph


class WeightedGridGraph(GridGraph):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.weights = {}

    def get_transition_cost(self, node):
        return self.weights.get(node, 1)