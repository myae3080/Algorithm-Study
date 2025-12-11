# source : https://www.acmicpc.net/problem/16360

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        word = input().rstrip()
        
        if word[-1] == 'a' or word[-1] == 'u':
            print(word +'s')
        elif word[-1] == 'i' or word[-1] == 'y':
            print(word[:-1] +'ios')
        elif word[-1] == 'l' or word[-1] == 'r' or word[-1] == 'v':
            print(word + 'es')
        elif word[-1] == 'n':
            print(word[:-1] + 'anes')
        elif word[-2:] == 'ne':
            print(word[:-2] + 'anes')
        elif word[-1] == 'o':
            print(word + 's')
        elif word[-1] == 't' or word[-1] == 'w':
            print(word + 'as')
        else:
            print(word + 'us')

if __name__ == '__main__':
    main()