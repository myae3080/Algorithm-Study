# source : https://www.acmicpc.net/problem/1681

import sys

def main():
    # input
    n, l = map(int, input().split())
    
    cnt = 0
    for i in range(1, sys.maxsize):
        if str(i).count(str(l)) == 0:
            cnt += 1
            
        if cnt == n:
            print(i)
            break

if __name__ == '__main__':
    main()