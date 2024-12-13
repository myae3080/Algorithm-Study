# source : https://www.acmicpc.net/problem/9724

import sys
input = sys.stdin.readline

def main():
    # input
    for i in range(1, int(input()) + 1):
        # input
        A, B = map(int, input().split())
        
        result = 0
        for n in range(int(A ** (1 / 3)), int(B ** (1 / 3)) + 1):
            if A <= n ** 3 <= B:
                result += 1
        
        print('Case #%d: %d' % (i, result))

if __name__ == '__main__':
    main()