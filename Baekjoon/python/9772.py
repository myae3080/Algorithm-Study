# source : https://www.acmicpc.net/problem/9772

import sys

input = sys.stdin.readline

def main():
    while 1:
        try:
            # input
            x, y = map(float, input().split())
            
            if x == 0 or y == 0:
                print('AXIS')
            elif x > 0 and y > 0:
                print('Q1')
            elif x > 0 and y < 0:
                print('Q4')
            elif x < 0 and y > 0:
                print('Q2')
            else:
                print('Q3')
        except:
            break

if __name__ == '__main__':
    main()