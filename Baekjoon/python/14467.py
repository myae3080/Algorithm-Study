# source : https://www.acmicpc.net/problem/14467

cows = {}
result = 0
for _ in range(int(input())):
    # input
    cow, location = map(int, input().split())
    
    if cow in cows and cows[cow] != location:
        cows[cow] = location
        result += 1
    else:
        cows[cow] = location
        
print(result)