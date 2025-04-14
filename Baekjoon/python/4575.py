# source : https://www.acmicpc.net/problem/4575

import sys

input = sys.stdin.readline

def main():
    while 1:
        # input
        sentence = input().rstrip()
        
        if 'END' == sentence:
            break
        
        has_dup = False
        for i in range(26):
            if sentence.count(chr(90 - i)) > 1:
                has_dup = True
                
                break
        
        if not has_dup:
            print(sentence)

if __name__ == '__main__':
    main()