from queue import Queue
from heapq import heappush, heappop
from math import sqrt

def path_finder(maze):
    maze_arr = maze_str_to_array(maze)
    n = len(maze_arr)
    start, goal = (0,0), (n-1, n-1)
    return ai_star(maze_arr, start, goal)

def bfs(maze_arr,start, goal):
    to_be_expanded = Queue()
    to_be_expanded.put(start)
    tree = set()

    while not to_be_expanded.empty():
        node = to_be_expanded.get()
        if node == goal:
            return True
        tree.add(node)
        neighbors = get_node_neighbors(maze_arr, node)
        for neighbor in neighbors:
            if neighbor not in tree:
                to_be_expanded.put(neighbor)
    return False

def ai_star(maze_arr, start, goal):
    to_be_expanded = []
    heappush(to_be_expanded, (manhattan_distance(start, goal),0, 0, start))
    tree = set()

    while to_be_expanded:
        _, cost, real_cost, node = heappop(to_be_expanded)
        if node == goal:
            return real_cost
        tree.add(node)
        neighbors = get_node_neighbors(maze_arr, node)
        for neighbor in neighbors:
            if neighbor not in tree:
                heappush(to_be_expanded, (cost + manhattan_distance(neighbor, goal), cost + 0.99, real_cost + 1, neighbor))
    return False

def manhattan_distance(cell, goal):
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

def euclidean_distance(cell, goal):
    return sqrt((cell[0] - goal[0])**2 + (cell[1] - goal[1])**2)

def maze_str_to_array(maze):
    return [[1 if char == "." else 0 for char in row] for row in maze.split("\n")]

def get_node_neighbors(maze_arr, parent_node):
    n = len(maze_arr)
    neighbors = []
    x_0, y_0 = parent_node
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        x_1 = x_0 + dx
        y_1 = y_0 + dy
        if 0 <= x_1 < n and 0 <= y_1 < n and maze_arr[y_1][x_1] == 1:
            neighbors.append((x_1, y_1))
    return neighbors

