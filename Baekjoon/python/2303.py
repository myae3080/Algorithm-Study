# source : https://www.acmicpc.net/problem/2303

score = 0
for i in range(int(input())):
    # input
    cards = list(map(int, input().split()))
    
    max_sum = 0
    size = len(cards)
    for a in range(size):
        for b in range(a + 1, size):
            for c in range(b + 1, size):
                max_sum = max(max_sum, int(str(cards[a] + cards[b] + cards[c])[-1]))
    
    if max_sum >= score:
        score = max_sum
        winner = i + 1

print(winner)