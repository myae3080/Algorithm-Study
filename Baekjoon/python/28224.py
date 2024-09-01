# source : https://www.acmicpc.net/problem/28224

import sys
input = sys.stdin.readline

def main():
    # input
    print(sum([int(input()) for _ in range(int(input()))]))

if __name__ == '__main__':
    main()