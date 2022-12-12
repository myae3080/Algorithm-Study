# source : https://www.acmicpc.net/problem/17356

# input
a, b = map(int, input().split())

m = (b - a) / 400
result = 1 / (1 + 10 ** m)

print(result)