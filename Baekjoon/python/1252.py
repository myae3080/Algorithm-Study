# source : https://www.acmicpc.net/problem/1252
# math

# input
a, b = input().split()

print(bin(int(a, 2) + int(b, 2))[2:])