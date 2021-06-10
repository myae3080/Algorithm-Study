# greedy algorithm

# input
change = 1000 - int(input())

coin_list = [500, 100, 50 , 10, 5, 1]
coins = 0

for coin in coin_list:
    if change != 0:
        if change >= coin:
            coins += (change // coin)
            change %= coin
        else:
            continue
    else:
        break
    
print(coins)