# source : https://www.acmicpc.net/problem/33689

import sys

input = sys.stdin.readline

def main():
    # input
    print(len([1 for _ in range(int(input())) if input()[0] == 'C']))

if __name__ == '__main__':
    main()