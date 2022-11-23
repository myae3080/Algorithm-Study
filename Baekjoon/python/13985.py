# source : https://www.acmicpc.net/problem/13985

# input
expression = input().split()

print('YES') if int(expression[0]) + int(expression[2]) == int(expression[-1]) else print('NO')