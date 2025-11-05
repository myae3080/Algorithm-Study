# source : https://www.acmicpc.net/problem/5074

import sys

input = sys.stdin.readline

def main():
    while 1:
        # input
        start, duration = input().split()

        if start == duration == '00:00':
            break

        sh, sm = map(int, start.split(':'))
        dh, dm = map(int, duration.split(':'))

        hh = sh + dh
        mm = sm + dm
        if mm >= 60:
            hh += 1
            mm %= 60
        
        n = 0
        if hh >= 24:
            n = hh // 24
            hh %= 24
        
        print('%s:%s' % (str(hh).zfill(2), str(mm).zfill(2)), '+' + str(n) if n > 0 else '')
    
if __name__ == '__main__':
    main()