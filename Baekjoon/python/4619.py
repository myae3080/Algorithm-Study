# source : https://www.acmicpc.net/problem/4619

import sys

def main():
    while 1:
        # input
        b, n = map(int, input().split())
        
        if b == n == 0:
            break
            
        if n == 1:
            print(b)
            continue
        
        prev, a = sys.maxsize, 1
        for i in range(1, b):
            diff = abs(b - (i ** n))
            
            if diff <= prev:
                prev = diff
                a = i
            else:
                break
        
        print(a)
    
if __name__ == '__main__':
    main()