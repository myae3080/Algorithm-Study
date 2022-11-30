# source : https://www.acmicpc.net/problem/13416

for _ in range(int(input())):
    result = 0
    for __ in range(int(input())):
        # input
        data = map(int, input().split())
        
        stock = max(data)
        if stock > 0:
            result += stock
        
    print(result)