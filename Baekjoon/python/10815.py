# sorting, binary search

import sys

# input
input = sys.stdin.readline

n = int(input())
sangeun_card_list = sorted(list(map(int, input().split())))
m = int(input())
card_list = list(map(int, input().split()))

result_list = [0] * m

for i in range(m):
    start, end = 0, n - 1
    card = card_list[i]

    while start <= end:
        mid_num = (start + end) // 2

        if sangeun_card_list[mid_num] == card:
            result_list[i] = 1
            break
        elif sangeun_card_list[mid_num] > card:
            end = mid_num - 1
        else:
            start = mid_num + 1

[print(n, end=' ') for n in result_list]