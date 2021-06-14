# data structure

from collections import deque
import sys

# input
minutes = int(input())

deq = deque()
total_score = 0

for m in range(minutes):
    temp_list = list(map(int, sys.stdin.readline().split()))

    if temp_list[0] == 1:
        deq.append(temp_list[1:])

    if deq:
        task_list = deq.pop()

        task_list[1] -= 1

        if task_list[1] == 0:
            total_score += task_list[0]
        else:
            deq.append(task_list)

print(total_score)