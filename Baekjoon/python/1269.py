# source : https://www.acmicpc.net/problem/1269

# input
a, b = map(int, input().split())
a_set, b_set = set(map(int, input().split())), set(map(int, input().split()))

print(len(a_set - b_set) + len(b_set - a_set))