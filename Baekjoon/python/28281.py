# source : https://www.acmicpc.net/problem/28281

import sys

def main():
    # input
    n, x = map(int, input().split())
    socks = list(map(int, input().split()))
    
    print(x * min([socks[i] + socks[i + 1] for i in range(n - 1)]))
    
if __name__ == '__main__':
    main()