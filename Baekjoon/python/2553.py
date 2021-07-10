# math, number theory

import sys, math

# input
input = sys.stdin.readline

n = int(input())

for s in str(math.factorial(n))[::-1]:
    if s != '0':
        print(s)
        break