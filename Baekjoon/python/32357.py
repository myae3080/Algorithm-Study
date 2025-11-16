# source : https://www.acmicpc.net/problem/32357

import sys

input = sys.stdin.readline

def main():
    # input
    N = int(input())

    palidrome_cnt = 0
    for _ in range(N):
        # input
        s = input().rstrip()

        mid = len(s) // 2
        if s[:mid] == s[mid:][::-1]:
            palidrome_cnt += 1
    
    print(palidrome_cnt * (palidrome_cnt - 1))
    
if __name__ == '__main__':
    main()