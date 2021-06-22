# math, brute force

def convert(num, base):
    sum = 0

    while num > 0:
        sum += num % base
        num //= base

    return sum

for i in range(1000, 10000):
    if convert(i, 10) == convert(i, 12) == convert(i, 16):
        print(i)