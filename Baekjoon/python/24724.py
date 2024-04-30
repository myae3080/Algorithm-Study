# source : https://www.acmicpc.net/problem/24724

import sys
input = sys.stdin.readline

def main():
    # input
    for i in range(1, int(input()) + 1):
        # input
        n = int(input())
        a, b = map(int, input().split())
        
        for __ in range(n):
            # input
            u, v = map(int, input().split())
        
        print('Material Management', i)
        print('Classification ---- End!')

if __name__ == '__main__':
    main()