# source : https://www.acmicpc.net/problem/12015
# binary search, LIS

# TODO : 이분 탐색 구현으로 풀어보기

from bisect import bisect_left

# input
n = int(input())
seq = list(map(int, input().split()))

dp = []

for num in seq:
    if len(dp) == 0 or num > dp[-1]:
        dp.append(num)
    else:
        dp[bisect_left(dp, num)] = num

print(len(dp))