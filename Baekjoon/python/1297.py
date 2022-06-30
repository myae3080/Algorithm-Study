# source : https://www.acmicpc.net/problem/1297

# input
d, h, w = map(int, input().split())

d_ratio = ((h ** 2) + (w ** 2)) ** 0.5

print(int((d * h) // d_ratio), int((d * w) // d_ratio))