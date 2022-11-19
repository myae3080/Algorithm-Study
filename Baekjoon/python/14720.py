# source : https://www.acmicpc.net/problem/14720

orders = {
    0: 1,
    1: 2,
    2: 0
}

# input
n = int(input())
milks = list(map(int, input().split()))

result, next = 0, 0
if milks[0] == 0:
    result += 1
    next = 1

for i in range(1, n):
    current = milks[i]
    if current == next:
        result +=1
        next = orders[current]

print(result)
           

