# source : https://www.acmicpc.net/problem/1009
# math

import sys

# input
input = sys.stdin.readline

for _ in range(int(input())):
    # input
    a, b = map(int, input().split())
    a %= 10
    
    if a == 0:
        print(10)  
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        b %= 2
        
        print((a ** 2) % 10) if b == 0 else print((a ** b) % 10)
    else:
        b %= 4
        
        print((a ** 4) % 10) if b == 0 else print((a ** b) % 10)