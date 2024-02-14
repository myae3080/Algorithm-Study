# source : https://www.acmicpc.net/problem/5698

import sys
input = sys.stdin.readline

def main():
    while 1:
        # input
        words = input().split()
        
        if words[0] == '*':
            break
        
        chars = set()
        for word in words:
            chars.add(word[0].lower())
        
        print('Y' if len(chars) == 1 else 'N')

if __name__ == '__main__':
    main()