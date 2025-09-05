# source : https://www.acmicpc.net/problem/12595

import sys

input = sys.stdin.readline

def main():
    # input
    for i in range(int(input())):
        # input
        G = int(input())
        C = list(map(int, input().split()))

        codes = {}
        for c in C:
            if c in codes:
                codes[c] += 1
            else:
                codes[c] = 1

        for k, v in codes.items():
            if v == 1:
                print('Case #%d: %d' % (i + 1, k))

                break

if __name__ == '__main__':
    main()