# source : https://www.acmicpc.net/problem/11094

import sys
input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        sentence = input().rstrip()
        
        if sentence.startswith('Simon says'):
            print(sentence[10:])

if __name__ == '__main__':
    main()