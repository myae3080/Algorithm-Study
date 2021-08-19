# source : https://www.acmicpc.net/problem/1475

import math

num_list = [0] * 10

for s in list(input()):
    if s == '6' or s == '9':
        num_list[6] += 0.5
    else:
        num_list[int(s)] += 1

print(int(math.ceil(max(num_list))))