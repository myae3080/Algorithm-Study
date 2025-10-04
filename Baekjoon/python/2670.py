# source : https://www.acmicpc.net/problem/2670

import sys

input = sys.stdin.readline

def main():
    # input
    N = int(input())
    nums = [float(input()) for _ in range(N)]

    dp = [1] * N
    dp[0] = nums[0]
    for i in range(1, N):
        dp[i] = max(dp[i - 1] * nums[i], nums[i])
    
    print('%0.3f' % max(dp))

if __name__ == '__main__':
    main()