# source : https://www.acmicpc.net/problem/11609

import sys

input = sys.stdin.readline

def main():
    # input
    names = [input().split() for _ in range(int(input()))]
    
    names.sort(key = lambda li: (li[1], li[0]))
    
    for name in names:
        print(' '.join(name))

if __name__ == '__main__':
    main()