# data structure, map

import sys

# input
input = sys.stdin.readline

k, l = map(int, input().split())
wait_dict = {}

# dict setting
for i in range(l):
    # input
    wait_dict[input().rstrip()] = i

for idx, tu in enumerate(sorted(wait_dict.items(), key=lambda tu: tu[1])):
    if idx > k - 1:
        break
    else:
        print(tu[0])