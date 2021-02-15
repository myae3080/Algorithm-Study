graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['C', 'E', 'F'],
    'E': [],
    'F': []
}

# def dfs(graph, start, visited):
#     visited.append(start)

#     print(visited)
    
#     for v in graph[start]:
#         if v not in visited:
#             dfs(graph, v, visited)

# dfs(graph, 'C', [])

# visited(list)를 parameter로 안 받는 방식
def dfs_list(graph, start):
    visited, nodeList = [], []

    nodeList.append(start)
    
    while nodeList:
        node = nodeList.pop(0)

        if node in visited:
            # 확인용
            print(node)
        else:
            visited.append(node)
            # start에 근접한 node 추가
            nodeList.extend(graph[node])
    
    return visited

#  정상적인 탐색 X, 수정 필요.
print(dfs_list(graph, 'C'))