# source : https://www.acmicpc.net/problem/5357

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        s = input().rstrip()
        
        result = ''
        for c in s:
            if not result or result[-1] != c:
                result += c
        
        print(result)

if __name__ == '__main__':
    main()