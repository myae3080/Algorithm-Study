# source : https://www.acmicpc.net/problem/1547

cups = [1, 2, 3]

for _ in range(int(input())):
    # input
    x, y = map(int, input().split())
    
    x_idx, y_idx = cups.index(x), cups.index(y)    
    cups[x_idx], cups[y_idx] = y, x

print(cups[0])