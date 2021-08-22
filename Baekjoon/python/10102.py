# source : https://www.acmicpc.net/problem/10102
# string

a, b = 0, 0

# input
n = int(input())
for s in input():
    if s == 'A':
        a += 1
    else:
        b += 1

print('A') if a > b else print('B') if b > a else print('Tie')