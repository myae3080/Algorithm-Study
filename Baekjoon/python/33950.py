# source : https://www.acmicpc.net/problem/33950

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        word = input().rstrip()

        while word.count('PO') > 0:
            word = word.replace('PO', 'PHO')
        
        print(word)

if __name__ == '__main__':
    main()