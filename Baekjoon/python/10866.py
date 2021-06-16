# deque

import sys
from collections import deque

input = sys.stdin.readline

deq = deque()

for i in range(int(input())):
    # input
    input_list = input().split()
    cmd = input_list[0]

    if cmd == 'push_front':
        deq.appendleft(input_list[1])
    elif cmd == 'push_back':
        deq.append(input_list[1])
    elif cmd == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif cmd == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(deq))
    elif cmd == 'empty':
        print(0) if deq else print(1)
    elif cmd == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    else:
        if deq:
            print(deq[-1])
        else:
            print(-1)