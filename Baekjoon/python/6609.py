# source : https://www.acmicpc.net/problem/6609

import sys
input = sys.stdin.readline

def main():
    while 1:
        try:
            # input
            M, P, L, E, R, S, N = map(int, input().split())
            
            for _ in range(N):
                prev_m = M
                # 성충
                M = P // S
                # 번데기
                P = L // R
                # 유충
                L = prev_m * E
            
            print(M)
        except:
            break

if __name__ == '__main__':
    main()