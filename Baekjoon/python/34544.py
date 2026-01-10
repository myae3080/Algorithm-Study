# source : https://www.acmicpc.net/problem/34544

import sys

input = sys.stdin.readline

def main():
    # input
    N = int(input())

    result = 1
    for _ in range(N):
        # input
        A, B = map(int, input().split())

        if A < 0 and B > 0:
            result += (B - A - 1)
        elif A > 0 and B < 0:
            result += (B - A + 1)
        else:
            result += (B - A)
    
    print(result if result > 0 else result - 1)

if __name__ == '__main__':
    main()