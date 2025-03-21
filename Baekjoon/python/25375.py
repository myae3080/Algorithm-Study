# source : https://www.acmicpc.net/problem/25375

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        a, b = map(int, input().split())
        
        print(1 if b % a == 0 and b / a >= 2 else 0)

if __name__ == '__main__':
    main()