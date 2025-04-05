# source : https://www.acmicpc.net/problem/11161

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        M = int(input())
        
        result, curr = 0, 0
        for _ in range(M):
            # input
            p_in, p_out = map(int, input().split())
            
            curr += (p_out - p_in)
            result = max(result, curr)
        
        print(result)

if __name__ == '__main__':
    main()