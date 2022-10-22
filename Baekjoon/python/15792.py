# source : https://www.acmicpc.net/problem/15792

# input
a, b = map(int, input().split())

result = str(a // b)
a %= b
if a != 0:
    result += '.'

for _ in range(1000):
    if a != 0:
        a *= 10
        result += str(a // b)
        a %= b

print(result)