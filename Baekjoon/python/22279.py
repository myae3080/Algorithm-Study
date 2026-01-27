# source : https://www.acmicpc.net/problem/22279

import sys

input = sys.stdin.readline

def main():
    # input
    N = int(input())

    qaly = 0
    for _ in range(N):
        # input
        q, y = map(float, input().split())

        qaly += q * y
    
    print(f"{qaly:.3f}")

if __name__ == '__main__':
    main()