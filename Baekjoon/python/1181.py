# string, sorting

import sys

# input
count = int(input())

str_list = []

for i in range(count):
    str_list.append(sys.stdin.readline().rstrip())

result_list = list(set(str_list))

# 다중 조건 정렬 방법
result_list.sort(key = lambda x : (len(x), x))

[print(s) for s in result_list]