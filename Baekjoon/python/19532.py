# source : https://www.acmicpc.net/problem/19532
# brute force, math

# input
a, b, c, d, e, f = map(int, input().split())

is_stop = False

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a * i) + (b * j) == c and (d * i) + (e * j) == f:
            print(i, j)
            is_stop = True
            
    if is_stop:
        break