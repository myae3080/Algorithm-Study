# source : https://www.acmicpc.net/problem/32498

import sys

input = sys.stdin.readline

def main():
    result = 0
    
    # input
    for _ in range(int(input())):
        # input
        if int(input()) % 2 == 1:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()