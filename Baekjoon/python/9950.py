# source : https://www.acmicpc.net/problem/9950

import sys
input = sys.stdin.readline

def main():
    while 1:
        # input
        a, b, c = map(int, input().split())
        
        if a == b == c == 0:
            break
        
        if a == 0:
            print(c // b, b, c)
        elif b == 0:
            print(a, c // a, c)
        else:
            print(a, b, a * b)

if __name__ == '__main__':
    main()