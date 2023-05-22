# source : https://www.acmicpc.net/problem/3943

import sys
input = sys.stdin.readline

def main():
    # input
    t = int(input())
    for _ in range(t):
        # input
        n = int(input())
        
        if n == 1:
            print(1)
        else:
            values = [n]
            while 1:
                if n % 2 == 0:
                    n //= 2
                else:
                    n = (n * 3) + 1
                
                values.append(n)
                
                if n == 1: 
                    break
            
            print(max(values))

if __name__ == '__main__':
    main()