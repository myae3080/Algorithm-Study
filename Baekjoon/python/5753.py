# source : https://www.acmicpc.net/problem/5753

import sys
input = sys.stdin.readline

def main():
    while 1:
        # input
        N, D = map(int, input().split())
        
        if N == D == 0:
            break
        
        result = [0] * N
        for _ in range(D):
            # input
            dinner = list(map(int, input().split()))
            
            for i in range(N):
                result[i] += dinner[i]
        
        print('yes' if max(result) == D else 'no')

if __name__ == '__main__':
    main()