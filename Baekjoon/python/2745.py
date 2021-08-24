# source : https://www.acmicpc.net/problem/2745
# string

# input
n, b = input().split()

n = n[::-1]
b = int(b)
result = 0

for i in range(len(n)):
    temp = int(n[i]) if n[i].isdigit() else (ord(n[i]) - 55)

    result += temp * (b ** i)

print(result)