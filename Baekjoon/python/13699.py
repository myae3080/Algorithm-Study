# source : https://www.acmicpc.net/problem/13699
# dp

# input
n = int(input())

dp = [1] * (n + 1)

for i in range(2, n + 1):
    a, b = 0, i - 1
    temp_sum = 0

    while b >= 0:
        temp_sum += dp[a] * dp[b]
        a += 1
        b -= 1
    
    dp[i] = temp_sum

print(dp[n])