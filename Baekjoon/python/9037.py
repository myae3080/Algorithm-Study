# source : https://www.acmicpc.net/problem/9037

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        N = int(input())
        candies = list(map(int, input().split()))
        
        if len(candies) == 1:
            print(0)
            
            continue
        
        candies = [c + 1 if c % 2 == 1 else c for c in candies]
        if len(set(candies)) == 1:
            print(0)
            
            continue
        
        result = 0
        while 1:
            result += 1
            gives = [0] * N
            for i in range(1, N + 1):
                prev, curr = i - 1, i
                if curr == N:
                    curr = 0
                
                half = candies[prev] // 2
                candies[prev] = half
                gives[curr] = half
            
            candies = [candies[i] + gives[i] for i in range(N)]
            candies = [c + 1 if c % 2 == 1 else c for c in candies]
            if len(set(candies)) == 1:
                break
        
        print(result)
            
if __name__ == '__main__':
    main()