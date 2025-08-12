# source : https://www.acmicpc.net/problem/10211

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        N = int(input())
        arr = list(map(int, input().split()))

        dp = [0] * N
        dp[0] = arr[0]
        for i in range(1, N):
            dp[i] = max(dp[i - 1] + arr[i], arr[i])
        
        print(max(dp))

if __name__ == '__main__':
    main()