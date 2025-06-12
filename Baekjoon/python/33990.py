# source : https://www.acmicpc.net/problem/33990

import sys

input = sys.stdin.readline

def main():
    # input
    rms = sorted([sum(list(map(int, input().split()))) for _ in range(int(input()))])
    
    if rms.count(512) > 0:
        print(512)

        return
    
    if rms[-1] < 512:
        print(-1)
        
        return
    
    for rm in rms:
        if rm > 512:
            print(rm)
            
            break

if __name__ == '__main__':
    main()