from queue import PriorityQueue
from dataclasses import dataclass

@dataclass
class Node:
    state : str
    path_cost : str
    parent : None


graph = {
    'A': [('B', 5), ('D', 12)],
    'B': [('A', 9), ('C', 4)],
    'C': [('D', 4), ('B', 7)],
    'D': [('A', 9), ('C', 5)]
}

goal = 'C'

def h(state):
    return abs(ord(goal) - ord(state))

def print_path(node:Node):
    path = []
    while node != None:
        path.append(node.state)
        node = node.parent
    path.reverse()
    print(" -> ".join(path))

def greedy_bfs(start:str, goal:str):
    frontier :list[Node] = [Node(start, h(start), None)] 
    explored: list[Node] = []

    while frontier:
        frontier.sort(key=lambda x: x.path_cost)
        node = frontier.pop(0)

        if node.state == goal:
            print("Reached goal! The path is:")
            print_path(node)
            return

        explored.append(node)

        for child in graph[node.state]:
            child_node = Node(child[0], h(child[0]), node)
            if child_node.state not in [t.state for t in explored] + [t.state for t in frontier]:
                frontier.append(child_node)
            else:
                for n in frontier:
                    if n.state == child_node.state and n.path_cost > child_node.path_cost:
                        n.parent = node




greedy_bfs('A', goal)