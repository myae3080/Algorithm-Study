# star

# input
n = int(input())

for i in range(1, 2 * n):
    print('*' * i) if i <= n else print('*' * (2 * n - i))