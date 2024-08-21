# source : https://www.acmicpc.net/problem/25858

import sys
input = sys.stdin.readline

def main():
    # input
    n, dollar = map(int, input().split())
    solves = [int(input()) for _ in range(n)]
    
    reward_per_solve = dollar // sum(solves)
    for s in solves:
        print(s * reward_per_solve)

if __name__ == '__main__':
    main()