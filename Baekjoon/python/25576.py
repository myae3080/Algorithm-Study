# source : https://www.acmicpc.net/problem/25576

import sys

input = sys.stdin.readline

def main():
    # input
    N, M = map(int, input().split())
    L = list(map(int, input().split()))

    bad_cnt = 0
    for _ in range(N - 1):
        # input
        K = list(map(int, input().split()))

        diff = 0
        for i in range(M):
            diff += abs(L[i] - K[i])
        
        if diff > 2000:
            bad_cnt += 1
    
    if bad_cnt * 2 >= N - 1:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()