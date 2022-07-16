# source : https://www.acmicpc.net/problem/10804

cards = [i for i in range(1, 21)]

for _ in range(10):
    # input
    a, b = map(int, input().split())
    
    cards[a - 1:b] = list(reversed(cards[a - 1:b]))
    
for n in cards:
    print(n, end=' ')