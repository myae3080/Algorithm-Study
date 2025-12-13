# source : https://www.acmicpc.net/problem/33674

from math import ceil

def main():
    # input
    N, D, K = map(int, input().split())
    stars = list(map(int, input().split()))

    min_day = min([K // s for s in stars])

    print(ceil(D / min_day) - 1)

if __name__ == '__main__':
    main()