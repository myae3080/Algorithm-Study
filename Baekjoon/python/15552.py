# fast io

import sys

# input
input_count = int(input())
int_list = []

for i in range(input_count):
    a, b = map(int, sys.stdin.readline().split())

    int_list.append(a + b)

for num in int_list:
    print(num)