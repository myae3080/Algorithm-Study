# source : https://www.acmicpc.net/problem/17608
# data structure, stack

import sys

# input
input = sys.stdin.readline

bar = []

# input
[bar.append(int(input())) for _ in range(int(input()))]

front_bar = bar.pop()
count = 1

for _ in range(len(bar)):
    temp_bar = bar.pop()

    if temp_bar > front_bar:
        count += 1
        front_bar = temp_bar

print(count)