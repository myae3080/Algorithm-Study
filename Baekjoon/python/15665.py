# source : https://www.acmicpc.net/problem/15665

# input
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

st = []
duplicate_check = set()

def dfs():
    if len(st) == m:
        sequence = ' '.join(map(str, st))
        
        if sequence not in duplicate_check:
            duplicate_check.add(sequence)
            print(sequence)
            
        return
    
    for i in range(n):
            st.append(nums[i])
            dfs()
            st.pop()

dfs()