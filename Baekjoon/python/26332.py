# source : https://www.acmicpc.net/problem/26332

import sys
input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        c, p = map(int, input().split())
        
        print(c, p)
        print((c * p) - ((c - 1) * 2))

if __name__ == '__main__':
    main()