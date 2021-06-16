# data structure, queue

import sys
from collections import deque

deq = deque()

'''
    list로 시도했지만, 시간 초과 때문에 deque 사용.
    list.pop과 deque.popleft 공부 필요
'''
for i in range(int(sys.stdin.readline())):
    # input
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