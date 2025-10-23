# source : https://www.acmicpc.net/problem/14535

import calendar, sys

input = sys.stdin.readline

def main():
    seq = 1
    while 1:
        # input
        N = int(input())

        if N == 0:
            break

        dates = [0] * 13
        for _ in range(N):
            # input
            dd, mm, yyyy = map(int, input().split())

            dates[mm] += 1
        
        print('Case #%d:' % seq)
        for i in range(1, 13):
            print('%s:%s' % (calendar.month_abbr[i], '*' * dates[i]))

        seq += 1

if __name__ == '__main__':
    main()