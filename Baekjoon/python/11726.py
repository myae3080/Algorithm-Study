# dp

# input
n = int(input())

max_n = 1001
dp_list = [0] * max_n

dp_list[1] = 1
dp_list[2] = 2

if n > 2:
    for i in range(3, n + 1):
        dp_list[i] = dp_list[i - 1] + dp_list[i - 2]

print(dp_list[n] % 10007)