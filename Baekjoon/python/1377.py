# source : https://www.acmicpc.net/problem/1377
# sorting

import sys

nums = []
cycle = 0

# input
[nums.append([int(sys.stdin.readline()), idx]) for idx in range(int(input()))]

sorted_nums = sorted(nums)

for i in range(len(nums)):
    cycle = max(cycle, sorted_nums[i][1] - i + 1)
    
print(cycle)