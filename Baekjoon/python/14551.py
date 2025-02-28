# source : https://www.acmicpc.net/problem/14551

import sys

input = sys.stdin.readline

def main():
    # input
    N, M = map(int, input().split())
    
    deck = 1
    for _ in range(N):
        # input
        A = int(input())
        
        if A != 0:
            deck *= A
        else:
            deck *= 1
    
    print(deck % M)

if __name__ == '__main__':
    main()