# Graph:
#                   A
#                  / \
#                /    \
#               B       C
#             / \     / | \ 
#            D   E - I  F  G
#                |         |
#                H        J
#
# DFS chooses a -> b -> e -> i 

from dataclasses import dataclass
 
@dataclass
class Node:
    state:str
    parent:str

graph = {
    'a' : ['c', 'b'],
    'b' : ['d', 'e'],
    'c' : ['f', 'g', 'i'],
    'd' : [],
    'e' : ['h', 'i'],
    'f' : [],
    'g' : ['j'],
    'h':[],
    'i':[],
    'j':[]
}

visited:list[Node] = []
queue:list[Node] = []

def print_path(visited:list[Node]):
    states = []
    cost = 0
    node = visited[len(visited)-1]
    states.append(node.state)
    while node.parent != None:
        cost += 1
        states.append(node.parent)
        index = [n.state for n in visited].index(node.parent)
        node = visited[index]
    states.reverse()
    print(" -> ".join(states))
    print(f'Total cost = {cost}')

def dfs(start_state, goal_state):
    found = False
    queue.append(Node(start_state, None))

    while len(queue) != 0:
        node = queue.pop()
        visited.append(node)

        if node.state == goal_state:
            found = True
            break;

        for neighbor in graph[node.state]:
            if neighbor not in [n.state for n in visited]+[n.state for n in queue]:
                queue.append(Node(neighbor, node.state))
    
    if found:
        print('Found the goal state. The path is:')
        print_path(visited)
    else:
        print('The goal state was not found in graph.')

dfs('a', 'i')
        