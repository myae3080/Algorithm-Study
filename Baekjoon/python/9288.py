# source : https://www.acmicpc.net/problem/9288

import sys
input = sys.stdin.readline

def main():
    # input
    for i in range(1, int(input()) + 1):
        # input
        n = int(input())
        
        print('Case %d:' % i)
        
        for a in range(1, 7):
            if 0 < n - a < 7 and a <= n - a:
                print('(%d,%d)' % (a, n - a))

if __name__ == '__main__':
    main()