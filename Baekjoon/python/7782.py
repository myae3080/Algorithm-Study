# source : https://www.acmicpc.net/problem/7782

import sys

input = sys.stdin.readline

def main():
    # input
    n = int(input())
    b1, b2 = map(int, input().split())
    coordinates = [list(map(int, input().split())) for _ in range(n)]
    
    for co in coordinates:
        if co[0] <= b1 and co[2] >= b1 and co[1] <= b2 and co[-1] >= b2:
            print('Yes')
            
            return
    
    print('No')

if __name__ == '__main__':
    main()