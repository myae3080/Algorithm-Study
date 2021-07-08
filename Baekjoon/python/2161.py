# data structure, deque, queue

from collections import deque

deq = deque()

# input
for i in range(1, int(input()) + 1):
    deq.append(i)

while len(deq) > 1:
    print(deq.popleft(), end=' ')

    deq.append(deq.popleft())

print(deq[0])