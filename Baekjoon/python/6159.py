# source : https://www.acmicpc.net/problem/6159

# PyPy3

import sys
input = sys.stdin.readline

def main():
    # input
    n, s = map(int, input().split())
    cows = [int(input()) for _ in range(n)]
    
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if cows[i] + cows[j] <= s:
                count += 1
    
    print(count)

if __name__ == '__main__':
    main()