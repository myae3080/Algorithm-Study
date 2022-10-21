# source : https://www.acmicpc.net/problem/2863

# input
a, b = map(int, input().split())
c, d = map(int, input().split())

values = []
for i in range(4):
    values.append((a / c) + (b / d))
    a, b, c, d = c, a, d, b
    
print(values.index(max(values)))