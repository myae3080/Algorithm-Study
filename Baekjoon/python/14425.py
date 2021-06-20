# data structure, string, set

import sys

# input
input = sys.stdin.readline

set_count, string_count = map(int, input().split())

string_set = set()
count = 0

for i in range(set_count):
    string_set.add(input().rstrip())

for i in range(string_count):
    if input().rstrip() in string_set:
        count += 1

print(count)