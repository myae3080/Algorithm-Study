#  greedy algorithm, sorting

import math

time_list = []
count = 0
start = math.pow(2, 31)
end = 0

# input
for i in range(int(input())):
    time_list.append(list(map(int, input().split())))

for li in sorted(time_list, key=lambda t: (t[1], t[0])):
    if count == 0:
        start = min(li[0], start)
        end = max(li[1], end)
        count += 1
    else:
        if li[0] >= end:
            start = min(li[0], start)
            end = max(li[1], end)
            count += 1

print(count)