# source : https://www.acmicpc.net/problem/5361

prices = [350.34, 230.90, 190.55, 125.30, 180.90]

for _ in range(int(input())):
    counts = list(map(int, input().split()))
    
    print('${:.2f}'.format(sum([prices[i] * counts[i] for i in range(5)])))