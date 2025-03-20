# source : https://www.acmicpc.net/problem/12596

import sys

input = sys.stdin.readline

def main():
    # input
    for i in range(1, int(input()) + 1):
        # input
        G = int(input())
        codes = list(map(int, input().split()))
        
        for code in codes:
            if codes.count(code) == 1:
                print('Case #%d: %d' % (i, code))
                
                break

if __name__ == '__main__':
    main()