# counting sorting

import sys

# input
input = sys.stdin.readline

counting_list = [0] * 10001

for i in range(int(input())):
    counting_list[int(input())] += 1

for i in range(1, 10001):
    if counting_list[i] != 0:
        for j in range(counting_list[i]):
            print(i)