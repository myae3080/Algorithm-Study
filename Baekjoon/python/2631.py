# source : https://www.acmicpc.net/problem/2631
# dp, lis

# 다른 방법으로 풀어보려고 했으나, 결국 LIS를 이용하여 해결. 다른 방식도 고려해볼 것.

nums, count = [], 0

# input
n = int(input())
[nums.append(int(input())) for _ in range(n)]

lis = [1] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            lis[i] = max(lis[i], lis[j] + 1)

print(n - max(lis))