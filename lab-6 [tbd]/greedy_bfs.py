inputGraph = {
    'A': [('B', 5), ('D', 12)],
    'B': [('A', 9), ('C', 4)],
    'C': [('D', 4), ('B', 7)],
    'D': [('A', 9), ('C', 5)]
}

def greedy_bfs(graph,start:str, goal:str):
    queue = [start]
    visited = []

    while queue:
        queue = sorted(queue, key=lambda x: x[1])
        node = queue.pop()

        if node not in visited:
            visited.append(node)

            if node[0] == goal:
                break

            neighbours = graph[node[0]]
            
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited

print(greedy_bfs(inputGraph, ("A",15), 'C'))