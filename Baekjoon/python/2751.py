# sorting

import sys

# input 
num_count = int(input())
result_list = [int(sys.stdin.readline()) for i in range(num_count)]

result_list.sort()

for num in result_list:
    print(num)