# source : https://www.acmicpc.net/problem/16466

from collections import deque

def main():
    # input
    N = int(input())
    tickets = deque(sorted(list(map(int, input().split()))))
    
    ticket = 1
    while 1:
        if len(tickets) == 0:
            print(ticket)
            break
        
        if ticket == tickets.popleft():
            ticket += 1
        else:
            print(ticket)
            break

if __name__ == '__main__':
    main()