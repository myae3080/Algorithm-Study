# source : https://www.acmicpc.net/problem/17496

# input
N, T, C, P = map(int, input().split())

print((((N - 1) // T) * C) * P)