graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['C', 'E', 'F'],
    'E': [],
    'F': []
}

def dfs(graph, start, visited):
    visited.append(start)

    print(visited)
    
    for v in graph[start]:
        if v not in visited:
            dfs(graph, v, visited)

dfs(graph, 'A', [])