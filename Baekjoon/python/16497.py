# source : https://www.acmicpc.net/problem/16497

import sys
input = sys.stdin.readline

def main():
    # input
    N = int(input())
    checkouts = [list(map(int, input().split())) for _ in range(N)]
    books = int(input())
    
    days = [0] + [books] * 31
    is_possible = True
    for checkout in checkouts:
        for d in range(checkout[0], checkout[1]):
            if days[d] > 0:
                days[d] -= 1
            else:
                is_possible = False
                break
        
        if not is_possible:
            break
    
    print(1 if is_possible else 0)

if __name__ == '__main__':
    main()