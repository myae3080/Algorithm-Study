# source : https://www.acmicpc.net/problem/9297

import sys
input = sys.stdin.readline

def main():
    # input
    for i in range(1, int(input()) + 1):
        # input
        n, d = map(int, input().split())
        
        integer = n // d
        numerator = n % d 
        if integer != 0 and numerator != 0:
            print('Case %d: %d %s' % (i, integer, str(numerator) + '/' + str(d)))
        elif integer != 0:
            print('Case %d: %d' % (i, integer))
        elif numerator != 0:
            print('Case %d: %s' % (i, str(numerator) + '/' + str(d)))
        else:
            print('Case %d: %d' % (i, 0))

if __name__ == '__main__':
    main()