# source : https://www.acmicpc.net/problem/26561

import sys
input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        p, t = map(int, input().split())
        
        print(p + (t // 4) - (t // 7))

if __name__ == '__main__':
    main()