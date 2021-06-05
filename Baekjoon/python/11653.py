# math, factorization

# input
num = int(input())

divisor = 2

while num != 1:
    if num % divisor == 0:
        num //= divisor
        print(divisor)
    else:
        divisor += 1