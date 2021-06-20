# math, dp, combination

def factorial(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * factorial(n - 1)

for i in range(int(input())):
    # input
    n, m = map(int, input().split())

    if n == m:
        print(1)
    else:
        if n < m:
            n, m = m, n
        
        print(factorial(n) // (factorial(n -m) * factorial(m)))
