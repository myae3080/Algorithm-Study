# source : https://www.acmicpc.net/problem/15917

import sys
input = sys.stdin.readline

def main():
    squares = [2 ** i for i in range(32)]
    
    # input
    n = int(input())
    [print(1) if int(input()) in squares else print(0) for _ in range(n)]
        
if __name__ == '__main__':
    main()