# source : https://www.acmicpc.net/problem/18110

import sys

def main():
    input = sys.stdin.readline
    
    # input
    n = int(input())
    
    if n == 0:
        print(0)
        return
    
    # input
    levels = sorted([int(input()) for _ in range(n)])

    excluded = roundUp(n * 0.15)
    
    print(roundUp(sum(levels[excluded: n - excluded]) / (n - 2 * excluded)))

def roundUp(num: float) -> int:
    return round(num + 1e-12)

if __name__ == '__main__':
    main()