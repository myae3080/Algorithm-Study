# math, binomial coefficient

# input
n, k = map(int, input().split())

# factorial method
def factorial(n):
    return_num = 1

    for i in range(2, n + 1):
        return_num *= i

    return return_num

print(int(factorial(n) / (factorial(k) * factorial(n - k))))