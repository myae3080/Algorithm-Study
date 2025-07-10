# source : https://www.acmicpc.net/problem/30236

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        n = int(input())
        seq = list(map(int, input().split()))
        
        result = []
        for i in range(n):
            if not result:
                result.append(2 if seq[i] == 1 else 1)
            else:
                if result[-1] + 1 != seq[i]:
                    result.append(result[-1] + 1)
                else:
                    result.append(result[-1] + 2)
        
        print(result[-1])

if __name__ == '__main__':
    main()