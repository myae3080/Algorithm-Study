# source : https://www.acmicpc.net/problem/30617

import sys

input = sys.stdin.readline

def main():
    prev_left, prev_right = 0, 0
    
    fun = 0
    # input
    for _ in range(int(input())):
        # input
        lt, rt = map(int, input().split())
        
        if lt != 0 and prev_left == lt:
            fun += 1
        if rt != 0 and prev_right == rt:
            fun += 1
        if lt != 0 and lt == rt:
            fun += 1
        
        prev_left, prev_right = lt, rt
    
    print(fun)

if __name__ == '__main__':
    main()