# dp

import sys

# input
input = sys.stdin.readline

stair_list = []

# input, list setting
[stair_list.append(int(input())) for i in range(int(input()))]

length = len(stair_list)

if length > 2:
    dp_list = [0] * length

    dp_list[0] = stair_list[0]
    dp_list[1] = stair_list[0] + stair_list[1]
    dp_list[2] = max(stair_list[1] + stair_list[2], stair_list[0] + stair_list[2])

    for i in range(3, length):
        # 2, 1, 1 or 2
        dp_list[i] = (max(dp_list[i - 3] + stair_list[i - 1] + stair_list[i], dp_list[i - 2] + stair_list[i]))

    print(dp_list[-1])
else:
    print(sum(stair_list))