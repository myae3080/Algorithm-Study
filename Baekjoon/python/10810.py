# input
n, m = map(int, input().split())

basket_list = [0] * n

for i in range(m):
    from_num, to_num, ball_num = map(int, input().split())

    for j in range(from_num - 1, to_num):
        basket_list[j] = ball_num

[print(n, end=' ') for n in basket_list]