# math, dp, combination

factorial_list = [0] * 101
factorial_list[1], factorial_list[2] = 1, 2

for i in range(3, 101):
    factorial_list[i] = factorial_list[i - 1] * i

n, m = map(int, input().split())

print(factorial_list[n] // (factorial_list[m] * factorial_list[n - m]))