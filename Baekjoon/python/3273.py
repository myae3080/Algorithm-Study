# sorting, two pointer

import sys

# input
input = sys.stdin.readline
n = int(input())
seq_list = sorted(list(map(int, input().split())))
x = int(input())

left, right, result = 0, n - 1, 0

while left < right:
    temp = seq_list[left] + seq_list[right]

    if temp == x:
        result += 1
        left += 1
    elif temp > x:
        right -= 1
    else:
        left += 1

print(result)