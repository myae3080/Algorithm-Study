# source : https://www.acmicpc.net/problem/11508

# input
n = int(input())

result = 0
dairies = []

# input
[dairies.append(int(input())) for i in range(n)]

dairies.sort(reverse=True)

for i in range(n):
    if i % 3 != 2:
        result += dairies[i]
    
print(result)