# source : https://www.acmicpc.net/problem/15001

import sys
input = sys.stdin.readline

def main():
    # input
    n = int(input())
    locations = [int(input()) for _ in range(n)]
    
    result = 0
    for i in range(1, n):
        result += (locations[i] - locations[i - 1]) ** 2
    
    print(result)

if __name__ == '__main__':
    main()