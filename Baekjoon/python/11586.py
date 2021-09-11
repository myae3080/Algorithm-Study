# source : https://www.acmicpc.net/problem/11586
# string

mirror = []

# input
[mirror.append(input()) for _ in range(int(input()))]
status = int(input())

if status == 1:
    for s in mirror:
        print(s)
elif status == 2:
    for s in mirror:
        print(s[::-1])
else:
    for s in mirror[::-1]:
        print(s)