# source : https://www.acmicpc.net/problem/14916

# input
price = int(input())

rest = price % 5
result = price // 5

if price == 1 or price == 3:
    print(-1)
else:
    if rest % 2 == 0:
        result += rest // 2
    else:
        result += ((rest + 5) // 2) - 1
        
    print(result)