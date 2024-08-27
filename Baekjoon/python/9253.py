# source : https://www.acmicpc.net/problem/9253

import sys
input = sys.stdin.readline

def main():
    # input
    A, B, S = input(), input(), input()
    print('YES' if S in A and S in B else 'NO')

if __name__ == '__main__':
    main()