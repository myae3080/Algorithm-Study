# source : https://www.acmicpc.net/problem/14235

import sys

input = sys.stdin.readline

def main():
    # input
    n = int(input())
    
    values = []
    for _ in range(n):
        # input
        base = list(map(int, input().split()))
        
        if base[0] == 0:
            if len(values) == 0:
                print(-1)
            else:
                print(values.pop())
        else:
            values.extend(base[1:])
            values.sort()

if __name__ == '__main__':
    main()