# source : https://www.acmicpc.net/problem/21771

import sys

input = sys.stdin.readline

def main():
    # input
    R, C = map(int, input().split())
    rg, cg, rp, cp = map(int, input().split())
    strings = [input().rstrip() for _ in range(R)]
    
    p_cnt = 0
    for s in strings:
        p_cnt += s.count('P')
    
    print(0 if p_cnt == rp * cp else 1)

if __name__ == '__main__':
    main()