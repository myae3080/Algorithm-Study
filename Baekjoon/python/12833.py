# source : https://www.acmicpc.net/problem/12833

# input
a, b, c = map(int, input().split())

print(a^b) if c % 2 != 0 else print(a)