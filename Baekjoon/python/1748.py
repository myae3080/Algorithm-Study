# math

import math

# input
string_num = input()

length = len(string_num)
count = 0
count_list = [int(math.pow(10, n)) * 9 for n in range(length - 1)]
sum_list = [count_list[n] * (n + 1) for n in range(length - 1)]

count += (int(string_num) - sum(count_list)) * length

for i in range(length - 1):
    count += sum_list[i]

print(count)