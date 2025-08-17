# source : https://www.acmicpc.net/problem/15828

import sys
from collections import deque

input = sys.stdin.readline

def main():
    # input
    N = int(input())

    buffer = deque()

    while 1:
        # input
        packet = int(input())

        if packet == -1:
            break
        elif packet == 0:
            buffer.popleft()
        else:
            if len(buffer) < N:
                buffer.append(packet)
    
    if len(buffer) == 0:
        print('empty')
    else:
        print(*buffer)

if __name__ == '__main__':
    main()