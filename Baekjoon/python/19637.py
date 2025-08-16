# source : https://www.acmicpc.net/problem/19637

import sys

input = sys.stdin.readline

def main():
    # input
    N, M = map(int, input().split())

    conditions = []
    for _ in range(N):
        # input
        rank, power = input().split()

        conditions.append((int(power), rank))
    
    for _ in range(M):
        # input
        p = int(input())

        start, end = 0, len(conditions)
        while start < end:
            mid = (start + end) // 2

            if p <= conditions[mid][0]:
                end = mid
            else:
                start = mid + 1
        
        print(conditions[start][1])

if __name__ == '__main__':
    main()