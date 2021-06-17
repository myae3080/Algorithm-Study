# binary search

import sys

# input
input = sys.stdin.readline

n = int(input())
n_list = sorted(list(map(int, input().split())))
k = int(input())
k_list = list(map(int, input().split()))

result_list = [0] * k

for i in range(k):
    target_num = k_list[i]
    from_num, to_num = 0, n - 1

    while from_num <= to_num:
        mid = (from_num + to_num) // 2

        if target_num > n_list[mid]:
            from_num = mid + 1
        elif target_num < n_list[mid]:
            to_num = mid - 1
        else:
            result_list[i] = 1
            break

[print(n) for n in result_list]