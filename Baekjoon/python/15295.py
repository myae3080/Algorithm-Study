# source : https://www.acmicpc.net/problem/15295

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        K, N = map(int, input().split())

        print(K, N * (N + 3) // 2)

if __name__ == '__main__':
    main()