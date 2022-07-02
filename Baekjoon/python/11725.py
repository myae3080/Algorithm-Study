# source : https://www.acmicpc.net/problem/11725
# tree, graph, dfs, bfs

# TODO : bfs로 풀어보기

import sys
sys.setrecursionlimit(10 ** 6)

# input
input = sys.stdin.readline
n = int(input())

graph = {}
parent_by_visited = [0] * (n + 1)

for _ in range(n - 1):
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

def dfs(i = 1):
    for n in graph[i]:
        if parent_by_visited[n] == 0:
            parent_by_visited[n] = i
            dfs(n)

dfs()

[print(parent_by_visited[i]) for i in range(2, n + 1)]