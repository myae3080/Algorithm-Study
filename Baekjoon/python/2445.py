# star

# input
n = int(input())

for i in range(n - 1, 0, -1):
    star = (2 * n - (2 * i)) // 2

    print('*' * star + ' ' * (2 * i) + '*' * star)

for j in range(n):
    star = (2 * n - (2 * j)) // 2

    print('*' * star + ' ' * (2 * j) + '*' * star)