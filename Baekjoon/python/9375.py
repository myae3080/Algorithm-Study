# math, data structure, string, dictionary

import sys

# input
input = sys.stdin.readline

for i in range(int(input())):
    total = 1
    dict = {}

    for j in range(int(input())):
        # input
        cloth, type = input().rstrip().split()

        if dict.get(type):
            dict.get(type).append(cloth)
        else:
            dict[type] = [cloth]

    for key in dict.keys():
        length = len(dict[key])

        total *= (length + 1)
    
    print(total - 1)