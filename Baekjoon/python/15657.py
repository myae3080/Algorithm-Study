# source : https://www.acmicpc.net/problem/15657

# input
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

st = []

def dfs(num = 0):
    if len(st) == m:
        print(' '.join(map(str, st)))
        return
    
    for i in range(num, n):
        st.append(nums[i])
        dfs(i)
        st.pop()

dfs()