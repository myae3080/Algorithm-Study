# set

import sys

# input
input = sys.stdin.readline

s = set()

for i in range(int(input())):
    input_list = input().split()

    cmd = input_list[0]

    if len(input_list) != 1:
        x = int(input_list[1])

    if cmd == 'add':
        s.add(x)
    elif cmd == 'remove':
        s.discard(x)
    elif cmd == 'check':
        print(1) if x in s else print(0)
    elif cmd == 'toggle':
        s.discard(x) if int(x) in s else s.add(x)
    elif cmd == 'all':
        s = set([n for n in range(1, 21)])
    else:
        s.clear()