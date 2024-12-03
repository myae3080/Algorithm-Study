# source : https://www.acmicpc.net/problem/17530

import sys
input = sys.stdin.readline

def main():
    # input
    votes = [int(input()) for _ in range(int(input()))]
    
    carlos = votes[0]
    
    if carlos >= max(votes):
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    main()