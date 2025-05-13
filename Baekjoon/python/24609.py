# source : https://www.acmicpc.net/problem/24609

import sys

input = sys.stdin.readline

def main():
    bank = 0
    result = 0
    
    # input
    for _ in range(int(input())):
        # input
        money = int(input())
        
        bank += money
        if bank < 0:
            result = max(result, abs(bank))
    
    print(result)

if __name__ == '__main__':
    main()