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

# 리스트를 이용한 bfs 구현
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

# print(bfs(graph, 'A'))

#  deque를 이용하 bfs 구현
def bfs_with_deque(graph, start):
    visited = []

    # print(deque([start]))
    return visited