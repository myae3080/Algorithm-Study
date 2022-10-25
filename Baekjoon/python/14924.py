# source : https://www.acmicpc.net/problem/14924

# input
S, T, D = map(int, input().split())

print((D // (2 * S)) * T)