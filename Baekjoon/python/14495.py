# source : https://www.acmicpc.net/problem/14495
# dp

# input
n = int(input())

dp = [1] * (n + 1)

if n >= 4:
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 3]

print(dp[n])