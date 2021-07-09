# math, divide and conquer

# input
a, b, mod = map(int, input().split())

def multiply(num):
    if num != 1:
        temp = multiply(num // 2)
        # even
        if num % 2 == 0:
            return (temp * temp) % mod
        # odd
        else:
            return (temp * temp * a) % mod
    else:
        return a % mod

print(multiply(b))