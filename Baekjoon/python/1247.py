# source : https://www.acmicpc.net/problem/1247

# TODO : java로 풀어보기

import sys
input = sys.stdin.readline

for _ in range(3):
    # input
    total = sum([int(input()) for __ in range(int(input()))])
    
    if total == 0:
        print(0)
    elif total > 0:
        print('+')
    else:
        print('-')