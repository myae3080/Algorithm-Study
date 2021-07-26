# source : https://www.acmicpc.net/problem/17175
# dp

dp_list = [0] * 51
dp_list[0], dp_list[1] = 1, 1

for i in range(2, 51):
    dp_list[i] = dp_list[i - 2] + dp_list[i - 1] + 1

# input
print(dp_list[int(input())] % 1000000007)