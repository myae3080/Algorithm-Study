# source : https://www.acmicpc.net/problem/6571
# math, dp

dp = [0] * 1001
dp[1], dp[2] = 1, 2

for i in range(3, 1001):
    dp[i] = dp[i - 1] + dp[i - 2]

while True:
    # input
    a, b = map(int, input().split())
    
    if a == 0 and b == 0:
        break
    
    result = 0
    
    for i in range(1, 1001):
        num = dp[i]
        
        if num > b:
            break
        elif a <= num <= b:
            result += 1
            
    print(result)