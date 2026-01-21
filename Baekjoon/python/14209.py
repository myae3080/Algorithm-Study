# source : https://www.acmicpc.net/problem/14209

import sys

input = sys.stdin.readline

def main():
    result = 0

    # input
    for _ in range(int(input())):
        # input
        cards = input().rstrip()

        result += cards.count('A') * 4 + cards.count('K') * 3 + cards.count('Q') * 2 + cards.count('J')
    
    print(result)

if __name__ == '__main__':
    main()