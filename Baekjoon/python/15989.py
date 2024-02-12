# source : https://www.acmicpc.net/problem/15989

# 규칙성을 찾다가 실패하고, 다른 사람들 해설 도움을 받음.

import sys
input = sys.stdin.readline

def main():
    # dp[0] = 0 인 경우로, 시도했지만, 코드가 더러워짐.
    dp = [1] * 10001
    
    # 2 더해지는 경우
    for i in range(2, 10001):
        dp[i] += dp[i - 2]
    
    # 3 더해지는 경우
    for i in range(3, 10001):
        dp[i] += dp[i - 3]
    
    # input
    for i in range(int(input())):
        # input
        print(dp[int(input())])

if __name__ == '__main__':
    main()