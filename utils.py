def from_id_width(id, rows):
    return id % rows, id // rows


def place_obstacles_util(graph, start, end, row=-1, col=-1):
    obstacles = []
    o = (-1, -1)
    for x in range(min(start, end), max(start, end)+1):
        if col >= 0:
            o = (x, col)
        elif row >= 0:
            o = (row, x)
        obstacles.append(o)
    graph.obstacles += obstacles


def place_vertical_obstacles(graph):
    for i in range(5, graph.cols-4, 5):
        place_obstacles_util(graph, 2-(3*(i%2)), graph.rows-(3*(i%2)), col=i)


def place_horizontal_obstacles(graph):
    for i in range(3, graph.rows-2, 3):
        place_obstacles_util(graph, 2-(3*(i%2)), graph.cols-(3*(i%2)), row=i)


def draw_tile(graph, id, style, width):
    r = "."
    if 'number' in style and id in style['number']: r = "%d" % style['number'][id]
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1: r = "v"
        if x2 == x1 - 1: r = "^"
        if y2 == y1 + 1: r = ">"
        if y2 == y1 - 1: r = "<"
    if 'start' in style and id == style['start']: r = "S"
    if 'goal' in style and id == style['goal']: r = "G"
    if 'path' in style and id in style['path']: r = "@"
    if id in graph.obstacles: r = "#" * width
    return r


def draw_grid(graph, width=2, **style):
    for x in range(graph.rows):
        for y in range(graph.cols):
            print("%%-%ds" % width % draw_tile(graph, (x, y), style, width), end="")
        print()


# WALLS = [from_id_width(id, width=30) for id in [21, 22, 51, 52, 81, 82, 93, 94, 111, 112, 123, 124, 133, 134, 141, 142, 153, 154, 163, 164, 171, 172, 173, 174, 175, 183, 184, 193, 194, 201, 202, 203, 204, 205, 213, 214, 223, 224, 243, 244, 253, 254, 273, 274, 283, 284, 303, 304, 313, 314, 333, 334, 343, 344, 373, 374, 403, 404, 433, 434]]


def place_obstacles_weights(graph):
    obstacles = [(7, 1), (8, 1), (7, 2), (8, 2), (7, 3), (8, 3)]
    nodes_to_weight_yx = [(3, 4), (3, 5),
                          (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8),
                          (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8),
                          (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7),
                          (7, 3), (7, 4), (7, 5)]
    nodes_to_weight = [(node[1], node[0]) for node in nodes_to_weight_yx]
    weights = {loc: 5 for loc in nodes_to_weight}
    graph.obstacles = obstacles
    graph.weights = weights


def heuristic(from_node, to_node):
    # Manhattan distance on a square grid
    return abs(from_node[0] - to_node[0]) + abs(from_node[1] - to_node[1])
