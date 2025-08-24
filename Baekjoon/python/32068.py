# source : https://www.acmicpc.net/problem/32068

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        L, R, S = map(int, input().split())

        L_distance, R_distance = S - L, R - S
        if R_distance > L_distance:
            print(L_distance * 2 + 1)
        else:
            print(R_distance * 2)

if __name__ == '__main__':
    main()