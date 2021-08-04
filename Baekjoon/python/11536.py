# source : https://www.acmicpc.net/problem/11536
# string, sorting

names = []

# input
[names.append(input()) for _ in range(int(input()))]

asc_names = sorted(names)
desc_names = sorted(names, reverse=True)

print('INCREASING') if names == asc_names else print('DECREASING') if names == desc_names else print('NEITHER')