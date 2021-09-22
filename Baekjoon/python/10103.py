# source : https://www.acmicpc.net/problem/10103
# math

chang, sang = 100, 100

for _ in range(int(input())):
    c, s = map(int, input().split())

    if c > s:
        sang -= c
    elif c < s:
        chang -= s

print(chang)
print(sang)