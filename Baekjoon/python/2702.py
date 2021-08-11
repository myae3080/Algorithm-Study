# source : https://www.acmicpc.net/problem/2702
# math, brute force, number theory

import sys

# input
input = sys.stdin.readline

def gcd(a, b):
    if a > b: 
        a, b = b, a

    if a == 0:
        return b
    else:
        return gcd(b % a, a)

def lcm(a, b):
    return (a * b) // gcd(a, b)

for _ in range(int(input())):
    # input
    a, b = map(int, input().split())

    print(lcm(a, b), gcd(a, b))