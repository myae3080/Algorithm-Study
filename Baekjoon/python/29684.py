# source : https://www.acmicpc.net/problem/29684

import sys

input = sys.stdin.readline

def main():
    while 1:
        # input
        n = int(input())

        if n == 0:
            break

        seconds = list(map(int, input().split()))

        diff = [abs(sec - 2023) for sec in seconds]

        print(diff.index(min(diff)) + 1)

if __name__ == '__main__':
    main()