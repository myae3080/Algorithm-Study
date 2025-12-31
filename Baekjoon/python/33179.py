# source : https://www.acmicpc.net/problem/33179

from math import ceil

def main():
    # input
    n = int(input())
    pages = list(map(int, input().split()))

    result = 0
    for page in pages:
        result += ceil(page / 2)
    
    print(result)

if __name__ == '__main__':
    main()