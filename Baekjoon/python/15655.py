# source : https://www.acmicpc.net/problem/15655

# input
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

st = []

def dfs(num = 0):
    if len(st) == m:
        print(' '.join(map(str, st)))
        return
    
    for i in range(num, n):
        if nums[i] not in st:
            st.append(nums[i])
            dfs(i + 1)
            st.pop()

dfs()