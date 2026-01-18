# source : https://www.acmicpc.net/problem/28239

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        b = bin(int(input()))[2:]

        result = []
        length = len(b)
        for i in range(length):
            if b[i] == '1':
                result.append(length - i - 1)
        
        if len(result) == 1:
            print(result[0] - 1, result[0] - 1)
        else:
            print(result[1], result[0])

if __name__ == '__main__':
    main()