# source : https://www.acmicpc.net/problem/9657

# input
n = int(input())

dp = [1] * (n + 1)

if n >= 2:
    dp[2] = 0
    
    for i in range(5, n + 1):
        if dp[i - 4] and dp[i - 3] and dp[i - 1]:
            dp[i] = 0
        
print("SK") if dp[n] else print("CY")