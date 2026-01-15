# source : https://www.acmicpc.net/problem/9056

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        a, b = input().split()

        if set(list(a)) == set(list(b)):
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()