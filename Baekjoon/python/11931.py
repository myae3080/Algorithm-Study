# sorting

import sys

# input
input = sys.stdin.readline

result_list = []

# input
[result_list.append(int(input())) for _ in range(int(input()))]

[print(i) for i in sorted(result_list, reverse=True)]