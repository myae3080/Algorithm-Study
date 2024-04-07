# source : https://www.acmicpc.net/problem/11815

import sys
input = sys.stdin.readline

def main():
    # input
    n = int(input())
    test = list(map(int, input().split()))
    
    results = ['1' if num == int(int(num ** 0.5) ** 2) else '0' for num in test]
    
    print(' '.join(results))

if __name__ == '__main__':
    main()