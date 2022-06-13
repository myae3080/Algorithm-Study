# source : https://www.acmicpc.net/problem/1652
# string

# input
n = int(input())
room = [list(input()) for _ in range(n)]

width_count, height_count = 0, 0

# width
for li in room:
    dot = 0
    
    for i in range(n):
        if  li[i] == '.':
            dot += 1
        else:
            if dot >= 2:
                width_count += 1
                
            dot = 0
    
    if dot >= 2:
        width_count += 1
        

# height
for i in range(n):
    dot = 0
    
    for j in range(n):
        if  room[j][i] == '.':
            dot += 1
        else:
            if dot >= 2:
                height_count += 1
                
            dot = 0
    
    if dot >= 2:
        height_count += 1

print(width_count, height_count)