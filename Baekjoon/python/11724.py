# graph theory, grapy search, bfs, dfs

import sys

# input
input = sys.stdin.readline
n, m = map(int, input().split())

graph = {}
count = 0
visited = [False] * (n + 1)

# graph setting
for _ in range(m):
    # input
    a, b = map(int, input().split())

    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)

    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)

def bfs(start):
    qu = [start]
    visited[start] = True

    while qu:
        temp = qu.pop(0)

        # KeyError 방지
        if temp in graph:
            for j in graph[temp]:
                if not visited[j]:
                    visited[j] = True
                    qu.append(j)

for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        bfs(i)

print(count)