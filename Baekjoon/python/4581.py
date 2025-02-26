# source : https://www.acmicpc.net/problem/4581

import sys

input = sys.stdin.readline

def main():
    while 1:
        # input
        records = input().rstrip()
        
        if records == '#':
            break
        
        yes, no, absent = 0, 0, 0
        for v in records:
            if v == 'Y':
                yes += 1
            elif v == 'N':
                no += 1
            elif v == 'A':
                absent += 1
        
        if absent >= len(records) / 2:
            print('need quorum')
        elif yes == no:
            print('tie')
        elif yes > no:
            print('yes')
        else:
            print('no')

if __name__ == '__main__':
    main()