# source : https://www.acmicpc.net/problem/15650

# input
n, m = map(int, input().split())

st = []

def dfs(num = 1):
    if len(st) == m:
        print(' '.join(map(str, st)))
        return
    
    for i in range(num, n + 1):
        if i not in st:
            st.append(i)
            dfs(i + 1)
            st.pop()

dfs()