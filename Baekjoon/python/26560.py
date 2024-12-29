# source : https://www.acmicpc.net/problem/26560

import sys
input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        sentence = input().rstrip()

        if sentence[-1] != '.':
            sentence += '.'
        
        print(sentence)

if __name__ == '__main__':
    main()