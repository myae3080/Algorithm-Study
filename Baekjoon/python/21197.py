# source : https://www.acmicpc.net/problem/21197

import sys

input = sys.stdin.readline

def main():
    # input
    N = int(input())
    times = [int(input()) for _ in range(N)]

    if N % 2 == 1:
        print('still running')
    else:
        result = 0
        for i in range(1, N, 2):
            result += (times[i] - times[i - 1])
        
        print(result)

if __name__ == '__main__':
    main()