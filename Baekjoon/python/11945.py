# source : https://www.acmicpc.net/problem/11945

# input
n, m = map(int, input().split())
[print(li[::-1]) for li in [input() for _ in range(n)]]