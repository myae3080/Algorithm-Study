# data structure, queue

from collections import deque
import sys

# input
input_count = int(input())

deq = deque()

for i in range(input_count):
    input_list = sys.stdin.readline().split()

    cmd = input_list[0]

    if cmd == 'push':
        deq.append(input_list[1])
    elif cmd == 'pop':
        print(deq.popleft()) if deq else print(-1)
    elif cmd == 'size':
        print(len(deq))
    elif cmd == 'empty':
        print(0) if deq else print(1)
    elif cmd == 'front':
        print(deq[0]) if deq else print(-1)
    else:
        print(deq[-1]) if deq else print(-1)