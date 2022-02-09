# source : https://www.acmicpc.net/problem/9251
# dp, LCS(Longest Common Subsequence)

# input
a, b = input(), input()

a_len, b_len = len(a), len(b)
dp = [[0] * (b_len+1) for _ in range(a_len+1)]

for i in range(1, a_len+1):
    temp_a = a[i-1]
    
    for j in range(1, b_len+1):
        temp_b = b[j-1]
        
        if temp_a == temp_b:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])