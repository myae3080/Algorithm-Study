# source : https://www.acmicpc.net/problem/9971

import sys

input = sys.stdin.readline

def main():
    while 1:
        # input
        line = input().rstrip()
        
        if line == 'ENDOFINPUT':
            break
        
        if line not in ('START', 'END'):
            print(''.join([cipherToPlain(c) if c.isupper() else c for c in line]))

def cipherToPlain(c: str) -> str:
    diff = 21
    
    return chr((ord(c) - ord('A') + diff) % 26 + ord('A'))

if __name__ == '__main__':
    main()