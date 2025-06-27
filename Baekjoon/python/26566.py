# source : https://www.acmicpc.net/problem/26566

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        A1, P1 = map(int, input().split())
        R1, P2 = map(int, input().split())
        
        if A1 / P1 > (R1 ** 2 * 3.14) / P2:
            print('Slice of pizza')
        else:
            print('Whole pizza')

if __name__ == '__main__':
    main()