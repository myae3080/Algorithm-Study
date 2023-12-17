# source : https://www.acmicpc.net/problem/2294

import sys

def main():
    # input
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    
    max_int = sys.maxsize
    dp = [0] + [max_int] * k
    for coin in coins:
        for v in range(coin, k + 1):
            dp[v] = min(dp[v], dp[v - coin] + 1)
    
    print(-1 if dp[k] == max_int else dp[k])

if __name__ == '__main__':
    main()