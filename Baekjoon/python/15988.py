# source : https://www.acmicpc.net/problem/15988
# dp

num = 1000000
divisor = 1000000009
dp_list = [0] * (num + 1)
dp_list[1], dp_list[2], dp_list[3] = 1, 2, 4

for i in range(4, (num + 1)):
    dp_list[i] = (dp_list[i - 3] % divisor) + (dp_list[i - 2] % divisor) + (dp_list[i - 1] % divisor)

[print(dp_list[int(input())] % divisor) for _ in range(int(input()))]