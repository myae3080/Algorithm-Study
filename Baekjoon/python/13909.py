# source : https://www.acmicpc.net/problem/13909

# input
n = int(input())

result, i = 1, 2
while i ** 2 < n:
    result += 1
    i += 1

print(result)