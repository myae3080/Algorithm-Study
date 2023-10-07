# source : https://www.acmicpc.net/problem/4998

import sys

def main():
    while 1:
        try:
            # input
            n, b, m = map(float, sys.stdin.readline().split())
            
            year = 1
            while 1:
                if n * (1 + b / 100) > m:
                    print(year)
                    break
                else:
                    n *= (1 + b / 100)
                    year += 1
        except:
            break

if __name__ == '__main__':
    main()