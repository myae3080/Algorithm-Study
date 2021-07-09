graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [6],
    5: [6, 7],
    6: [],
    7: [5]
}

# 큐를 이용한 bfs 구현
def queue_bfs(start):
    visited_list, qu = [start], [start]

    while qu:
        temp = qu.pop(0)

        for n in graph[temp]:
            if n not in visited_list:
                visited_list.append(n)
                qu.append(n)
    
    return visited_list

print(queue_bfs(2))