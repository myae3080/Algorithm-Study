# source : https://www.acmicpc.net/problem/5523

import sys
input = sys.stdin.readline

a, b = 0, 0
for _ in range(int(input())):
    # input
    A, B = map(int, input().split())
    
    if A > B :
        a += 1
    elif B > A:
        b += 1

print(a, b)