# source : https://www.acmicpc.net/problem/34414

import sys

input = sys.stdin.readline

def main():
    # input
    less_heights = ['cut' for _ in range(int(input())) if int(input()) < 48]

    print(len(less_heights) == 0)

if __name__ == '__main__':
    main()