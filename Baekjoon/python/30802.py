# source : https://www.acmicpc.net/problem/30802

from math import ceil

def main():
    # input
    N = int(input())
    sizes = list(map(int, input().split()))
    T, P = map(int, input().split())
    
    min_tshirt = 0
    for size in sizes:
        min_tshirt += ceil(size / T)
    
    print(min_tshirt)
    print(N // P, N % P)

if __name__ == '__main__':
    main()