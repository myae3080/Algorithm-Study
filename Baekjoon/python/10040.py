# source : https://www.acmicpc.net/problem/10040

import sys
input = sys.stdin.readline

def main():
    # input
    n, m = map(int, input().split())
    costs = [int(input()) for _ in range(n)]
    criteria = [int(input()) for _ in range(m)]
    
    votes = [0] * n
    for c in criteria:
        for i in range(n):
            if costs[i] <= c:
                votes[i] += 1
                break
    
    print(votes.index(max(votes)) + 1)

if __name__ == '__main__':
    main()