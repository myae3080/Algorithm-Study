# data structure, string

import sys

# input
input = sys.stdin.readline

name_set = set()

for i in range(int(input())):
    # input
    name, io = input().rstrip().split()

    if io == 'enter':
        name_set.add(name)
    else:
        name_set.remove(name)

[print(name) for name in sorted(name_set, reverse=True)]