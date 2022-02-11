# source : https://www.acmicpc.net/problem/7510
# math, geometry

for i in range(int(input())):
    # input
    squares = sorted([num ** 2 for num in list(map(int, input().split()))])
    
    result = "no"
    
    if sum(squares[:2]) == squares[2]:
        result = "yes"
    
    print("Scenario #" + str(i + 1) + ":")
    print(result)
    print()