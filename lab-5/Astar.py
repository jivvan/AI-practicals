# Implementation of A* search

from dataclasses import dataclass
from queue import PriorityQueue

@dataclass
class Node:
    state:str
    g_cost: int
    f_cost: int
    parent:str

graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
    'J': []
}

start = 'A'
goal = 'J'

def h(state:str):
    return abs(ord(goal) - ord(state))

def print_path(node:Node):
    path = []
    print('Total cost:', node.g_cost)
    while node != None:
        path.append(node.state)
        node = node.parent
    path.reverse()
    print(" -> ".join(path))

def a_star(start, goal):
    frontier :list[Node] = [Node(start, 0, h(start)+0, None)] 
    explored: list[Node] = []
    while frontier:
        frontier.sort(key=lambda x:x.f_cost)
        node = frontier.pop(0)
        
        if node.state == goal:
            print("Reached goal! The path is:")
            print_path(node)
            return
        
        explored.append(node)
        
        for child in graph[node.state]:
            c_g_cost = node.g_cost + child[1]
            child_node = Node(child[0], c_g_cost,c_g_cost+h(child[0]),node)
            if child_node.state not in [n.state for n in frontier]+[n.state for n in explored]:
                frontier.append(child_node)
            else:
                for n in frontier:
                    if n.state == child_node.state and n.g_cost > child_node.g_cost:
                        n.parent = node

a_star(start, goal)
