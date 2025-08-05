# source : https://www.acmicpc.net/problem/26340

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        a, b, time = map(int, input().split())

        a_copy, b_copy = a, b
        for _ in range(time):
            if a_copy > b_copy:
                a_copy //= 2
            else:
                b_copy //= 2
        
        print('Data set: %d %d %d' % (a, b, time))
        print(max(a_copy, b_copy), min(a_copy, b_copy))
        print()

if __name__ == '__main__':
    main()