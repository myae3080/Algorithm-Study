# source : https://www.acmicpc.net/problem/4909

import sys

input = sys.stdin.readline

def main():
    while 1:
        # input
        scores = list(map(int, input().split()))

        if sum(scores) == 0:
            break

        scores.sort()

        avg = sum(scores[1:5]) / 4
        if int(avg) == avg:
            print(int(avg))
        else:
            print(avg)

if __name__ == '__main__':
    main()