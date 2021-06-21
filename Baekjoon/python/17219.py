# data structure

import sys

# input
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())


id_pw_dict = {}

for i in range(n):
    id, pw = input().rstrip().split()

    id_pw_dict[id] = pw

for j in range(m):
    print(id_pw_dict[input().rstrip()])