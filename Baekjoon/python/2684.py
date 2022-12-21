# source : https://www.acmicpc.net/problem/2684

for _ in range(int(input())):
    # input
    coins = input()
    
    rule = {'H': '1', 'T': '0'}
    seq_count = [0] * 8
    for i in range(38):
        sequence = '0b'
        
        for coin in coins[i:i + 3]:
            sequence += rule[coin]
        
        seq_count[int(sequence, 2)] += 1
        
    print(' '.join([str(num) for num in seq_count]))