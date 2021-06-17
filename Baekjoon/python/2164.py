# data structure, queue

from collections import deque

count = 1

# input
deq = deque([n for n in range(1, int(input()) + 1)])

while len(deq) > 1:
    if (count % 2) == 1:
        deq.popleft()
    else:
        deq.append(deq.popleft())

    count += 1

print(deq.pop())