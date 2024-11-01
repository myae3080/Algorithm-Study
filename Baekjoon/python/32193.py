# source : https://www.acmicpc.net/problem/32193

import sys
input = sys.stdin.readline

def main():
    height = 0
    
    # input
    for _ in range(int(input())):
        # input
        A, B = map(int, input().split())
        
        height = A - B + height
        
        print(height)

if __name__ == '__main__':
    main()