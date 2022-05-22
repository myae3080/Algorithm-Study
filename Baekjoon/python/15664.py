# source : https://www.acmicpc.net/problem/15664

# input
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

st = []
visited = [0] * len(nums)
duplicate_check = set()

def dfs(num = 0):
    if len(st) == m:
        sequence = ' '.join(map(str, st))
        
        if sequence not in duplicate_check:
            duplicate_check.add(sequence)
            print(sequence)
            
        return
    
    for i in range(num, n):
        if not visited[i]:
            st.append(nums[i])
            visited[i] = 1
            dfs(i + 1)
            st.pop()
            visited[i] = 0

dfs()