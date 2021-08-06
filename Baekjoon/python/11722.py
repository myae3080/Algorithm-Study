# source : https://www.acmicpc.net/problem/11722
# dp

# input
n = int(input())
seq_list = list(map(int, input().split()))

len_list = [1] * n

for i in range(1, n):
    for j in range(i):
        if seq_list[i] < seq_list[j]:
            len_list[i] = max(len_list[i], len_list[j] + 1)

print(max(len_list))