# source : https://www.acmicpc.net/problem/21613

import sys

input = sys.stdin.readline

def main():
    result = ''
    money = 0
    
    # input
    for _ in range(int(input())):
        # input
        name, bid = input().rstrip(), int(input())
        
        if bid > money:
            result = name
            money = bid
    
    print(result)

if __name__ == '__main__':
    main()