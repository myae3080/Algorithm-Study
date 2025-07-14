# source : https://www.acmicpc.net/problem/25893

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        stats = list(map(int, input().split()))
        
        print(*stats)
        
        stats10_cnt = 0
        for stat in stats:
            if stat >= 10:
                stats10_cnt += 1
        
        if stats10_cnt == 0:
            print('zilch')
        elif stats10_cnt == 1:
            print('double')
        elif stats10_cnt == 2:
            print('double-double')
        else:
            print('triple-double')
        print()

if __name__ == '__main__':
    main()