# source : https://www.acmicpc.net/problem/7581

import sys
input = sys.stdin.readline

def main():
    while 1:
        # input
        a, b, c, v = map(int, input().split())
        
        if a == b == c == v == 0:
            break
        
        if v == 0:
            print(a, b, c, a * b * c)
        else:
            if a == 0:
                print(v // (b * c), b, c, v)
            elif b == 0:
                print(a, v // (a * c), c, v)
            else:
                print(a, b, v // (a * b), v)

if __name__ == '__main__':
    main()