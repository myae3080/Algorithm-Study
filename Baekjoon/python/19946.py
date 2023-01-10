# source : https://www.acmicpc.net/problem/19946

# input
n = int(input())

k = 64
while not n % 2:
    n //= 2
    k -= 1

print(k)