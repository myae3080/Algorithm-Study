# source : https://www.acmicpc.net/problem/14729
# sorting

import sys

input = sys.stdin.readline

# input
scores = [float(input().rstrip()) for i in range(int(input()))]

scores.sort()

[print('{:.3f}'.format(scores[i])) for i in range(7)]