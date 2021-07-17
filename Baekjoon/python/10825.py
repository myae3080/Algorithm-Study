# sorting

import sys

# input
input = sys.stdin.readline

data_list = []

# input
[data_list.append(input().rstrip().split()) for _ in range(int(input()))]

# sorting
data_list.sort(key=lambda li: (-int(li[1]), int(li[2]), -int(li[3]), li[0]))

[print(li[0]) for li in data_list]