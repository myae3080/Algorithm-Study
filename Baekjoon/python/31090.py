# source : https://www.acmicpc.net/problem/31090

import sys
input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        year = input()
        
        print('Good' if not (int(year) + 1) % int(year[2:4]) else 'Bye')

if __name__ == '__main__':
    main()