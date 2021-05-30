# greedy

# input
people_num = int(input())
time_list = list(map(int, input().split()))

# variable
sum_time = 0
accumulated_time = 0

time_list.sort()

for minute in time_list:
    accumulated_time += minute
    sum_time += accumulated_time

print(sum_time)

