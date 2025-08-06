# source : https://www.acmicpc.net/problem/13228

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        x1, y1, f1, x2, y2, f2 = map(int, input().split())

        print(abs(x1 - x2) + abs(y1 - y2) + f1 + f2)

if __name__ == '__main__':
    main()