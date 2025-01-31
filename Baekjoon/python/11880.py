# source : https://www.acmicpc.net/problem/11880

import sys
input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        a, b, c = map(int, input().split())
        
        print(min(a ** 2 + (b + c) ** 2, b ** 2 + (a + c) ** 2, c ** 2 + (a + b) ** 2))

if __name__ == '__main__':
    main()