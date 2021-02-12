# Fibonacci
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# 실행 결과
print(fib(7))