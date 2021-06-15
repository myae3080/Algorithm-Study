# sorting

location_list = []

# input
[location_list.append(list(map(int, input().split()))) for i in range(int(input()))]

location_list.sort()

[print(li[0], li[1]) for li in location_list]