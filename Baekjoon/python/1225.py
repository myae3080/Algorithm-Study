# source : https://www.acmicpc.net/problem/1225

# input
num1, num2 = input().split()

result = 0

num1_sum = sum([int(c1) for c1 in num1])

for c2 in num2:
    result += num1_sum * int(c2)

print(result)