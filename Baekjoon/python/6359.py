# source : https://www.acmicpc.net/problem/6359

for _ in range(int(input())):
    # input
    n = int(input())
    
    rooms = [True] * (n + 1)
    
    for i in range(2, n + 1):
        for k in range(i, n + 1, i):
            rooms[k] = not rooms[k]
                
    print(rooms[1:].count(True))