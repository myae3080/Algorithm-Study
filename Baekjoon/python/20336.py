# source : https://www.acmicpc.net/problem/20336

import sys

input = sys.stdin.readline

def main():
    # input
    menus = [input().split() for _ in range(int(input()))]

    for item in menus[0]:
        print(item)

if __name__ == '__main__':
    main()