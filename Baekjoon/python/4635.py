# source : https://www.acmicpc.net/problem/4635

import sys

input = sys.stdin.readline

def main():
    while 1:
        # input
        n = int(input())
        
        if n == -1:
            break
        
        result = 0
        d = 0
        for _ in range(n):
            # input
            s, t = map(int, input().split())
            
            result += s * (t - d)
            d = t
        
        print('%d miles' % result)

if __name__ == '__main__':
    main()