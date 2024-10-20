# source : https://www.acmicpc.net/problem/11645

import sys
input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        cities = set([input().rstrip() for _ in range(int(input()))])
        
        print(len(cities))

if __name__ == '__main__':
    main()