# source : https://www.acmicpc.net/problem/1246

import sys

input = sys.stdin.readline

def main():
    # input
    N, M = map(int, input().split())
    prices = sorted([int(input()) for _ in range(M)])
    
    max_price, max_profit = 0, 0
    for i in range(M):
        if min((M - i), N) * prices[i] > max_profit:
            max_price = prices[i]
            max_profit = min((M - i), N) * prices[i]
    
    print(max_price, max_profit)

if __name__ == '__main__':
    main()