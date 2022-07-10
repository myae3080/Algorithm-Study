# source : https://www.acmicpc.net/problem/1568
# math

# input
n = int(input())

result, k  = 0, 1

while n > 0:
    if n < k:
        k = 1
        
    n -= k
    result += 1
    k += 1

print(result)