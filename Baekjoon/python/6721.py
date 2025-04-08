# source : https://www.acmicpc.net/problem/6721

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        num1, num2 = input().split()
        
        print(int(str(int(num1[::-1]) + int(num2[::-1]))[::-1]))

if __name__ == '__main__':
    main()