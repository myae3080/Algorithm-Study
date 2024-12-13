# source : https://www.acmicpc.net/problem/3448

import sys
input = sys.stdin.readline

def main():
    # input
    N = int(input())
    
    for _ in range(N):
        R, A = 0, 0
        
        while 1:
            # input
            line = input().rstrip()
            
            if line == '':
                break
            
            for c in line:
                if c == '#':
                    A += 1
                else:
                    A += 1
                    R += 1
        
        ratio = round((R / A) * 100, 1)
        if ratio == int(ratio):
            ratio = int(ratio)
        
        print('Efficiency ratio is %s%%.' % str(ratio))

if __name__ == '__main__':
    main()