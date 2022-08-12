# source : https://www.acmicpc.net/problem/25304

from functools import reduce

# input
print('Yes') if int(input()) == sum([reduce(lambda x, y: x * y, map(int, input().split())) for _ in range(int(input()))]) else print('No')