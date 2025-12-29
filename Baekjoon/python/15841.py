# source : https://www.acmicpc.net/problem/15841

import sys

input = sys.stdin.readline

def main():
    fibo = [0] * 491
    fibo[1] = 1
    for i in range(2, 491):
        fibo[i] = fibo[i - 1] + fibo[i - 2]

    while 1:
        # input
        hour = int(input())

        if hour == -1:
            break

        print('Hour %d: %d cow(s) affected' % (hour, fibo[hour]))

if __name__ == '__main__':
    main()