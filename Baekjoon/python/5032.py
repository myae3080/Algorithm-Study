# source : https://www.acmicpc.net/problem/5032

# input
e, f, c = map(int, input().split())

empty = e + f
result = 0
while empty // c:
    beverage = empty // c 
    result += beverage
    empty = beverage + (empty % c)
    
print(result)