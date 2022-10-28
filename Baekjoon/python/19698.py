# source : https://www.acmicpc.net/problem/19698

# input
n, w, h, l = map(int, input().split())

print(min((w // l) * (h // l), n))