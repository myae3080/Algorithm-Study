# source : https://www.acmicpc.net/problem/11053
# dp, LIS

# input
n = int(input())
seq_list = list(map(int, input().split()))

# 0을 default로 잡고 풀 시에, 반례 존재.
'''
    5
    3 2 2 2 3
'''
len_list = [1] * n

# 일반적인 풀이법, O(N^2)
for i in range(1, n):
    for j in range(i):
        if seq_list[i] > seq_list[j]:
            len_list[i] = max(len_list[i], len_list[j] + 1)
    
print(max(len_list))