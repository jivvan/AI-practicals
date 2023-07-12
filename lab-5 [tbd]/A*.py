# Implementation of A* search
# TODO: DO BETTER MAN!!! THIS CODE IS A PILE OF SHIT
from dataclasses import dataclass
from queue import PriorityQueue

@dataclass
class Node:
    state:str
    heuristic: int
    parent:str

Graph_nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
}

def print_path(visited:list[Node]):
    states = []
    cost = 0
    node = visited[len(visited)-1]
    states.append(node.state)
    while node.parent != None:
        cost += node.heuristic
        states.append(node.parent)
        index = [n.state for n in visited].index(node.parent)
        node = visited[index]
    states.reverse()
    print(" -> ".join(states))
    print(f'Total cost = {cost}')

def a_star(start_state, goal_state):
    p_queue = PriorityQueue(10)
    visited:list[Node]= []
    start_node = Node(start_state, 0, None)
    p_queue.put((start_node.heuristic, start_node))
    found = False
    while not p_queue.empty():
        _, node = p_queue.get()
        visited.append(node)

        if node.state == goal_state:
            found = True
            break

        for neighbour, heuristic in Graph_nodes[node.state]:
            if neighbour not in [n.state for n in visited]:
                p_queue.put((heuristic,Node(neighbour, heuristic, node.state)))
    if found:
        print('Found the final state. The path is:')
        print_path(visited)
    else:
        print('The state was not found in graph.')

a_star('A', 'H')
