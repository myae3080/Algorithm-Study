# source : https://www.acmicpc.net/problem/4158
# dictinonary

import sys
input = sys.stdin.readline

while True:
    # input
    n, m = map(int, input().split())
    
    if n == 0 and m == 0:
        break
    
    cds = {}
    count = 0

    for _ in range(n):
        # input
        cds[int(input())] = 1
        
    for _ in range(m):
        # input
        if int(input()) in cds:
            count += 1
        
    print(count)