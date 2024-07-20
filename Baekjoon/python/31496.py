# source : https://www.acmicpc.net/problem/31496

import sys
input = sys.stdin.readline

def main():
    # input
    N, S = input().split()
    
    result = 0
    for _ in range(int(N)):
        # input
        item, quantity = input().split()
        
        if S in item.split('_'):
            result += int(quantity)
    
    print(result)

if __name__ == '__main__':
    main()