# source : https://www.acmicpc.net/problem/28225

import sys

input = sys.stdin.readline

def main():
    # input
    n, f = map(int, input().split())

    velocity = []
    for _ in range(n):
        # input
        x, v = map(int, input().split())

        velocity.append((f - x) / v)
    
    print(velocity.index(min(velocity)) + 1)

if __name__ == '__main__':
    main()