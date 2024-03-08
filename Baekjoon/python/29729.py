# source : https://www.acmicpc.net/problem/29729

import sys
input = sys.stdin.readline

def main():
    # input
    s, n, m = map(int, input().split())
    
    using = 0
    for _ in range(n + m):
        # input
        command = input().rstrip()

        if command == '1':
            if s == using:
                s *= 2
                
            using += 1
        else:
            using -= 1
    
    print(s)

if __name__ == '__main__':
    main()