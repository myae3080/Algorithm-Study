# source : https://www.acmicpc.net/problem/15813
# string

result = 0

# input
n = int(input())
for c in input():
    result += ord(c) - 64

print(result)