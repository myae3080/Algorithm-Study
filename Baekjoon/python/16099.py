# source : https://www.acmicpc.net/problem/16099

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        lt, wt, le, we = map(int, input().split())

        t, e = lt * wt, le * we
        if t > e:
            print('TelecomParisTech')
        elif e > t:
            print('Eurecom')
        else:
            print('Tie')

if __name__ == '__main__':
    main()