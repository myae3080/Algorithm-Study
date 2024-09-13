# source : https://www.acmicpc.net/problem/24783

import sys
input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        a, b, c = map(int, input().split())
        
        if a + b == c:
            print('Possible')
            continue
        elif abs(a - b) == c:
            print('Possible')
            continue
        elif a * b == c:
            print('Possible')
            continue
        elif max(a, b) / min(a, b) == c:
            print('Possible')
            continue
        else:
            print('Impossible')

if __name__ == '__main__':
    main()