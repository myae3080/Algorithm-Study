# source : https://www.acmicpc.net/problem/5919

import sys
input = sys.stdin.readline

def main():
    # input
    N = int(input())
    hay_bales = [int(input()) for _ in range(N)]
    
    equal_height = sum(hay_bales) // N
    
    result = 0
    for bale in hay_bales:
        if equal_height > bale:
            result += equal_height - bale
    
    print(result)

if __name__ == '__main__':
    main()