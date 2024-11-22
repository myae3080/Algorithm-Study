# source : https://www.acmicpc.net/problem/11522

import sys
input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        K, N = map(int, input().split())
        
        S1 = N * (N + 1) // 2
        S2 = N ** 2
        S3 = (2 * N * ((2 * N) + 1) // 2) - S2
        
        print(K, S1, S2, S3)

if __name__ == '__main__':
    main()