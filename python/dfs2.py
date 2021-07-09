graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [6],
    5: [6, 7],
    6: [],
    7: [5]
}

# 재귀로 푸는 방식.
def recursive_dfs(v, visited=[]):
    visited.append(v)

    for i in graph[v]:
        if not i in visited:
            visited = recursive_dfs(i, visited)
    
    return visited

print(recursive_dfs(1, []))

# stack으로 푸는 방식
def stack_dfs(v):
    visited_list = []
    stack = [v]

    while stack:
        # 마지막
        temp = stack.pop()

        if temp not in visited_list:
            visited_list.append(temp)

            for t in graph[temp]:
                stack.append(t)

    return visited_list

print(stack_dfs(1))