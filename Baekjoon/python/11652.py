# data structure, sorting

import sys

# input
input = sys.stdin.readline

num_dict = {}

for i in range(int(input())):
    input_num = int(input())

    if input_num in num_dict:
        num_dict[input_num] += 1
    else:
        num_dict[input_num] = 1
    
max_value = max(num_dict.values())

for key in sorted(num_dict):
    if num_dict[key] == max_value:
        print(key)
        break