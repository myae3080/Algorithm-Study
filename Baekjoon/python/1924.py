# input
m, d = map(int, input().split())

month_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_list = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day_num = 0

for i in range(m):
    day_num += month_list[i]

day_num += d

print(day_list[day_num % 7])