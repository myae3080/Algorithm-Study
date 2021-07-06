# math

square_list = [False] * 10001

for i in range(1, 101):
    square_list[i ** 2] = True

# input
n = int(input())
m = int(input())

min_square = 20000
sum_square = 0

for i in range(n, m + 1):
    if square_list[i]:
        min_square = min(min_square, i)
        sum_square += i

if sum_square == 0:
    print(-1)
else:
    print(sum_square)
    print(min_square)