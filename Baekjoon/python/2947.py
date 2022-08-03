# source : https://www.acmicpc.net/problem/2947

# input
trees = list(map(int, input().split()))

while True:
    orders = ''
    
    for i in range(len(trees) - 1):
        if trees[i] > trees[i + 1]:
            trees[i], trees[i + 1] = trees[i + 1], trees[i]
            
            orders = ' '.join([str(n) for n in trees])
            print(orders)
            
    if orders == '1 2 3 4 5':
        break