# source : https://www.acmicpc.net/problem/14470
# math

total = 0

# input
temp = int(input())
target_temp = int(input())
c, d, e = int(input()), int(input()), int(input())

if temp < target_temp:
    if temp < 0:
        total += temp * -1 * c
        temp = 0

    if temp == 0:
        total += d

    if temp < target_temp:
        diff = target_temp - temp
        total += diff * e

print(total)