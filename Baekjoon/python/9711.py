# source : https://www.acmicpc.net/problem/9711

import sys

input = sys.stdin.readline

def main():
    fibo = [0, 1, 1]
    for i in range(3, 10001):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    
    # input
    for i in range(1, int(input()) + 1):
        # input
        P, Q = map(int, input().split())

        print('Case #%d: %d' % (i, fibo[P] % Q))

if __name__ == '__main__':
    main()