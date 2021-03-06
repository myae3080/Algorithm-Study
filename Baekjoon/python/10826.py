# dp, fibonacci

# input
n = int(input())

if n > 2:
    fibo_list = [0] * (n + 1)
    fibo_list[1], fibo_list[2] = 1, 1

    for i in range(3, n + 1):
        fibo_list[i] = fibo_list[i - 1] + fibo_list[i - 2]

    print(fibo_list[n])
elif n == 0:
    print(0)
else:
    print(1)