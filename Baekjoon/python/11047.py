coin_num, sum = map(int, input().split())

coin_type_list = []
coin_count = 0

for i in range(0, coin_num):
    coin_type_list.append(int(input()))

coin_type_list.reverse()

for value in coin_type_list:
    if sum == 0:
        break

    value_by_coin = (sum // value)
    coin_count += value_by_coin

    sum -= value_by_coin * value

print(coin_count)
