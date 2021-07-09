# dfs, bfs

import sys
from collections import defaultdict

# input
input = sys.stdin.readline

vertex, node, start = map(int, input().split())

graph = defaultdict(list)

# graph setting
for i in range(node):
    s, e = map(int, input().split())

    graph[s].append(e)
    graph[e].append(s)

# sorting
for i in graph:
    graph[i].sort()

# dfs
def dfs(start, visited=[]):
    visited.append(start)

    for v in graph[start]:
        if v not in visited:
            visited = dfs(v, visited)

    return visited

# dfs output
dfs_result = dfs(start, [])

for i in range(len(dfs_result)):
    print(dfs_result[i], end=' ') if i != len(dfs_result) - 1 else print(dfs_result[i])

# bfs
def bfs(start):
    visited, qu = [start], [start]

    while qu:
        temp = qu.pop(0)

        for n in graph[temp]:
            if n not in visited:
                visited.append(n)
                qu.append(n)
    
    return visited

# bfs output 
bfs_result = bfs(start)

for i in range(len(bfs_result)):
    print(bfs_result[i], end=' ') if i != len(bfs_result) - 1 else print(bfs_result[i])