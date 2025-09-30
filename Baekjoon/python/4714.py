# source : https://www.acmicpc.net/problem/4714

import sys

input = sys.stdin.readline

def main():
    while 1:
        # input
        weight = float(input())

        if weight == -1:
            break

        print('Objects weighing %.2f on Earth will weigh %.2f on the moon.' % (weight, weight * 0.167))

if __name__ == '__main__':
    main()