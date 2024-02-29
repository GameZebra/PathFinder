from queue import Queue
from priority_queue import PriorityQueue
from grid_graph import GridGraph
from weighted_grid_graph import WeightedGridGraph
from utils import *


def main():
    # ----- enter number of graph rows and columns -----
    rows = 15  # read from console
    cols = 15  # read from console

    # ----- create graph -----
    # For BFS and GBF:
    #graph = GridGraph(rows, cols)

    # For Dijkstra and A* :
    graph = WeightedGridGraph(rows, cols)

    # Optional:
    # place_vertical_obstacles(graph)
    # place_horizontal_obstacles(graph)
    place_obstacles_weights(graph)

    # ----- set start and goal nodes -----
    start_node = (2, 5)  # read from console
    goal_node = (40, 15)  # read from console

    # ----- execute the search from start to goal -----
    # path = breadth_first_search(graph, start_node, goal_node)
    path, costs = dijkstra(graph, start_node, goal_node)
    # path = greedy_best_first(graph, start_node, goal_node)
    # path, costs = a_star(graph, start_node, goal_node)

    # ----- show results -----
    # For all algorithms:
    draw_grid(graph, width=3, point_to=path, start=start_node, goal=goal_node)
    print()
    # Only for Dijkstra and A* :
    draw_grid(graph, width=3, number=costs, start=start_node, goal=goal_node)
    print()
    # For all algorithms:
    draw_grid(graph, width=3, path=reconstruct_path(path, start=start_node, goal=goal_node))


def reconstruct_path(came_from, start, goal):
    # 1. create a list (this will be the resulting path)
    final_solution = []
    # 2. start from the goal node as current (current = goal)
    current = goal
    
    # 3. append the current node to the list
    # 4. find the current's predecessor (look it up in the dictionary)
    # 5. let the current be the predecessor
    # 6. repeat 3 - 5 until the current node becomes the start node
    while current != start:
        final_solution.append(current)
        current = came_from[current]
    # 7. return the resulting path and delete the pass keyword
    return final_solution


def breadth_first_search(graph, start_node, goal_node):
    # create a queue for discovered nodes
    discovered = []
    # put the start node into the queue
    discovered.append(start_node);
    # create a dictionary for keeping track of {successor: predecessor}
    family = {}
    # put the start node into the dictionary as key and None as value
    family[start_node] = None;
    # while there are nodes in the queue:
    while discovered != []:
    #   get a node (predecessor) from the queue and find its neighbors
        temp_parent = discovered.pop(0);
        if temp_parent == goal_node:
            break
        temp_neighbors = graph.get_neighbors(temp_parent)
    
    #   if the neighbor is not in the dictionary:                      <---\
    #       put the neighbor as a key and the predecessor as a value  <----\--(repeat for all neighbors)
    #       put the neighbor into the queue  
        for neighbor in temp_neighbors:
            if neighbor not in family:
                family[neighbor] = temp_parent
                discovered.append(neighbor)

    # return the dictionary and delete the pass keyword
    return family


def dijkstra(graph, start_node, goal_node):
    # create a priority queue for discovered nodes
    prio_queue = PriorityQueue()
    # put the start node with cost 0 into the queue
    prio_queue.put(start_node, 0)
    # dictionary {node: predecessor}
    family = {start_node: None}
    # dictionary {node: cost}
    travel_costs = {start_node: 0}

    # while there are nodes in the queue:
    while prio_queue.is_empty() == False:
        # get a predecessor from discovered nodes
        current_node = prio_queue.get()

        # if the predecessor node == goal node, break the loop
        if current_node == goal_node:
            break
        # find all neighbors of the predecessor node
        temp_neighbors = graph.get_neighbors(current_node)
        # for each neighbor:
        for neighbor in temp_neighbors:
            # calculate the new cost to this neighbor as:
            # cost to its predecessor + cost of the transition 'predecessor --> neighbor'
            new_cost = travel_costs[current_node] + graph.get_transition_cost(neighbor)
            # if neighbor is not discovered or its new cost is lower:
            discovered = prio_queue.get_queue()
            if neighbor not in discovered:
                # add the neighbor to the discovered nodes with its new cost
                prio_queue.put(neighbor, new_cost)
                # update the {node: predecessor} dictionary
                family[neighbor] = current_node
                # update the {node: cost} dictionary
                travel_costs[neighbor] = new_cost
        # return the {node: predecessor} and {node: cost} dictionaries; delete the pass keyword
        return family, travel_costs


def greedy_best_first(graph, start_node, goal_node):
    # Same as breadth-first, but
    # nodes are prioritized based on heuristics (e.g. Manhattan distance).
    pass


def a_star(graph, start_node, goal_node):
    # Same as Dijkstra but priority includes heuristics.
    pass


if __name__ == '__main__':
    main()

# myFunction()
# opravi mi koda;
