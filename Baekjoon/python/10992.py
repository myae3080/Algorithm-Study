# source : https://www.acmicpc.net/problem/10992

# input
n = int(input())

[print(' ' * (n - i) + '*' * ((2 * i) - 1)) if i == 1 or i == n else print(' ' * (n - i) + '*' +  ' ' * ((2 * (i - 1)) - 1) + '*') for i in range(1, n + 1)]