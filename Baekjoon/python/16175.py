# source : https://www.acmicpc.net/problem/16175

import sys
input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        n, m = map(int, input().split())
        votes = [list(map(int, input().split())) for _ in range(m)]
        
        candidates = [0] * n
        for i in range(n):
            for j in range(m):
                candidates[i] += votes[j][i]
        
        print(candidates.index(max(candidates)) + 1)

if __name__ == '__main__':
    main()