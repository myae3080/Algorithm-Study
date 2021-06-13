# prefix sum

import sys

# input
count = int(input())
prefix_sum_list = []

# 누적합 list 
for idx, num in enumerate(list(map(int, sys.stdin.readline().split()))):
    if idx == 0:
        prefix_sum_list.append(num)
    else:
        prefix_sum_list.append(prefix_sum_list[idx - 1] + num)

section_count = int(input())

for i in range(section_count):
    # input
    from_num, to_num = map(int, sys.stdin.readline().split())

    if from_num == 1:
        print(prefix_sum_list[to_num - 1])
    else:
        print(prefix_sum_list[to_num - 1] - prefix_sum_list[from_num - 2])