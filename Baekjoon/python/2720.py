# source : https://www.acmicpc.net/problem/2720

for _ in range(int(input())):
    # input
    cents = int(input())
    
    coins = {25: 0, 10: 0, 5: 0, 1: 0}
    
    for coin in coins.keys():
        coins[coin] = (cents // coin)
        cents %= coin
        
    [print(count, end=' ') for count in coins.values()]