# source : https://www.acmicpc.net/problem/8974

n = 0
sequence = []
for i in range(1, 300):
    sequence += [i] * i
    n += i
    
    if n > 1000:
        break
    
# input
a, b = map(int, input().split())

print(sum(sequence[a - 1:b]))