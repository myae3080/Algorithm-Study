# source : https://www.acmicpc.net/problem/28279

import sys, collections
input = sys.stdin.readline

def main():
    deq = collections.deque()
    
    # input
    for _ in range(int(input())):
        # input
        command = list(map(int, input().split()))
        
        c = command[0]
        if c == 1:
            deq.appendleft(command[1])
        elif c == 2:
            deq.append(command[1])
        elif c == 3:
            if not deq:
                print(-1)
            else:
                print(deq.popleft())
        elif c == 4:
            if not deq:
                print(-1)
            else:
                print(deq.pop())
        elif c == 5:
            print(len(deq))
        elif c == 6:
            print(1 if not deq else 0)
        elif c == 7:
            if not deq:
                print(-1)
            else:
                print(deq[0])
        else:
            if not deq:
                print(-1)
            else:
                print(deq[-1])

if __name__ == '__main__':
    main()