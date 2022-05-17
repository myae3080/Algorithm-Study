# source : https://www.acmicpc.net/problem/15654

# input
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

st = []

def dfs():
    if len(st) == m:
        print(' '.join(map(str, st)))
        return
    
    for i in range(n):
        if nums[i] not in st:
            st.append(nums[i])
            dfs()
            st.pop()

dfs()