# source : https://www.acmicpc.net/problem/20001
# data structure, stack

import sys

# input
input = sys.stdin.readline

stack = []

while True:
    # input
    input_str = input().rstrip()

    if input_str == '고무오리 디버깅 끝':
        break

    if input_str == '문제':
        stack.append(1)
    elif input_str == '고무오리':
        if len(stack) == 0:
            stack.append(1)
            stack.append(1)
        else:
            stack.pop()

print('고무오리야 사랑해') if len(stack) == 0 else print('힝구')