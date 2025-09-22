# source : https://www.acmicpc.net/problem/34027

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        N = int(input())

        sqrt = N ** 0.5
        
        print(1 if sqrt == int(sqrt) else 0)

if __name__ == '__main__':
    main()