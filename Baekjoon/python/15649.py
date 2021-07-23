# back tracking

# input
n, m = map(int, input().split())

st = []

# 재귀 실행 순서를 이해하는게 중요.
def dfs():
    if len(st) == m:
        print(' '.join(map(str, st)))
        return

    for i in range(1, n + 1):
        if i not in st:
            st.append(i)
            dfs()
            st.pop()
        else:
            continue

dfs()