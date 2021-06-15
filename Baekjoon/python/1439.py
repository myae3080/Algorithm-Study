# greedy algorithm

import math

# input
input_str = input()

change = 0

for i in range(1, len(input_str)):
    if input_str[i - 1] != input_str[i]:
        change += 1

print(math.ceil(change / 2))