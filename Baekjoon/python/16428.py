# source : https://www.acmicpc.net/problem/16428

import sys
input = sys.stdin.readline

# input
a, b = map(int, input().split())

q = a // b
r = a % b

if a != 0 and r < 0:
    q += 1
    r -= b
    
print(q)
print(r)