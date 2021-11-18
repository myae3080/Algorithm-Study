# source : https://www.acmicpc.net/problem/17284
# math

total = 0
vending_machine = {'1' : 500, '2' : 800, '3' : 1000}

# input
for i in input().split():
    total += vending_machine[i]
    
print(5000 - total)