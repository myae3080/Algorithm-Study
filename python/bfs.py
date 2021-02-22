graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['C', 'E', 'F'],
    'E': ['G'],
    'F': [],
    'G': ['E', 'H', 'I'],
    'H': [],
    'I': []
}

def bfs(graph, start):
    visited, to_visit = [], []
    
    to_visit = [start]

    while to_visit:
        current_node = to_visit.pop(0)

        if current_node not in visited:
            visited.append(current_node)
            to_visit.extend(graph[current_node])
            print(to_visit)

    return visited

print(bfs(graph, 'A'))