# source : https://www.acmicpc.net/problem/14471

import sys
input = sys.stdin.readline

def main():
    # input
    n, m = map(int, input().split())

    left_prize = m - 1
    cards = []
    for i in range(m):
        # input
        a, b = map(int, input().split())

        if a >= n:
            left_prize -= 1
        else:
            cards.append(a)
    
    if left_prize <= 0:
        print(0)
    else:
        cards.sort(reverse=True)

        result = 0
        for i in range(left_prize):
            result += (n - cards[i])
        
        print(result)

if __name__ == '__main__':
    main()