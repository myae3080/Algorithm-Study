# prefix num

import sys

# input
num_count, for_count = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

for i, num in enumerate(num_list):
    if i != 0:
        num_list[i] += num_list[i - 1]

for i in range(for_count):
    from_num, to_num = map(int, sys.stdin.readline().split())

    if from_num == to_num:
        if to_num == 1:
            print(num_list[to_num - 1])
        else:
            print(num_list[to_num - 1] - num_list[to_num - 2])
    else:
        if from_num == 1:
            print(num_list[to_num - 1])
        else:
            print(num_list[to_num - 1] - num_list[from_num - 2])