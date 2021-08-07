# source : https://www.acmicpc.net/problem/9507
# dp

dp = [1] * 71
dp[2], dp[3] = 2, 4

for i in range(4, 71):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]

[print(dp[int(input())]) for _ in range(int(input()))]