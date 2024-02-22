from queue import Queue
from priority_queue import PriorityQueue
from grid_graph import GridGraph
from weighted_grid_graph import WeightedGridGraph
from utils import *


def main():
    # ----- enter number of graph rows and columns -----
    rows = 0  # read from console
    cols = 0  # read from console

    # ----- create graph -----
    # For BFS and GBF:
    # graph = GridGraph(rows, cols)

    # For Dijkstra and A* :
    # graph = WeightedGridGraph(rows, cols)

    # Optional:
    # place_vertical_obstacles(graph)
    # place_horizontal_obstacles(graph)
    # place_obstacles_weights(graph)

    # ----- set start and goal nodes -----
    start_node = (0, 0)  # read from console
    goal_node = (0, 0)  # read from console

    # ----- execute the search from start to goal -----
    # path = breadth_first_search(graph, start_node, goal_node)
    # path, costs = dijkstra(graph, start_node, goal_node)
    # path = greedy_best_first(graph, start_node, goal_node)
    # path, costs = a_star(graph, start_node, goal_node)

    # ----- show results -----
    # For all algorithms:
    # draw_grid(graph, width=3, point_to=path, start=start_node, goal=goal_node)
    print()
    # Only for Dijkstra and A* :
    # draw_grid(graph, width=3, number=costs, start=start_node, goal=goal_node)
    print()
    # For all algorithms:
    # draw_grid(graph, width=3, path=reconstruct_path(path, start=start_node, goal=goal_node))


def reconstruct_path(came_from, start, goal):
    # 1. create a list (this will be the resulting path)

    # 2. start from the goal node as current (current = goal)


        # 3. append the current node to the list

        # 4. find the current's predecessor (look it up in the dictionary)

        # 5. let the current be the predecessor

    # 6. repeat 3 - 5 until the current node becomes the start node
    # 7. return the resulting path and delete the pass keyword

    pass


def breadth_first_search(graph, start_node, goal_node):
    # create a queue for discovered nodes

    # put the start node into the queue

    # create a dictionary for keeping track of {successor: predecessor}

    # put the start node into the dictionary as key and None as value

    # while there are nodes in the queue:

    #   get a node (predecessor) from the queue and find its neighbors


    #   if the neighbor is not in the dictionary:                      <---\
    #       put the neighbor as a key and the predecessor as a value  <----\--(repeat for all neighbors)
    #       put the neighbor into the queue                            <--- |

    # return the dictionary and delete the pass keyword

    pass


def dijkstra(graph, start_node, goal_node):
    # create a priority queue for discovered nodes

    # put the start node with cost 0 into the queue

    # dictionary {node: predecessor}

    # dictionary {node: cost}

    # while there are nodes in the queue:

        # get a predecessor from discovered nodes

        # if the predecessor node == goal node, break the loop

        # find all neighbors of the predecessor node

        # for each neighbor:

            # calculate the new cost to this neighbor as:
            # cost to its predecessor + cost of the transition 'predecessor --> neighbor'

            # if neighbor is not discovered or its new cost is lower:

                # add the neighbor to the discovered nodes with its new cost

                # update the {node: predecessor} dictionary

                # update the {node: cost} dictionary

        # return the {node: predecessor} and {node: cost} dictionaries; delete the pass keyword

    pass


def greedy_best_first(graph, start_node, goal_node):
    # Same as breadth-first, but
    # nodes are prioritized based on heuristics (e.g. Manhattan distance).
    pass


def a_star(graph, start_node, goal_node):
    # Same as Dijkstra but priority includes heuristics.
    pass


if __name__ == '__main__':
    main()
