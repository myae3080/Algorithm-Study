# source : https://www.acmicpc.net/problem/2870

import re

# input
words = [input() for _ in range(int(input()))]

numbers = []
for word in words:
    for str_num in re.findall(r'\d+', word):
        numbers.append(int(str_num))

[print(num, end='\n') for num in sorted(numbers)]