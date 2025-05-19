# source : https://www.acmicpc.net/problem/26532

from math import ceil

def main():
    # input
    x, y = map(int, input().split())
    
    acre = x * y / 4840
    
    print(ceil(acre / 5))

if __name__ == '__main__':
    main()