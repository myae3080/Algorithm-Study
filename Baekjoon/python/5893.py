# source : https://www.acmicpc.net/problem/5893

# input
n = input()

length = len(n) - 1
result = 0

for i, s in enumerate(n):
    result += (2 ** (length - i)) * int(s)

print(bin(result * 17)[2:])