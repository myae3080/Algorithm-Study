# source : https://www.acmicpc.net/problem/24416

# 시간초과로 Pypy3로 제출

# input
n = int(input())

global recursive
recursive = 1

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        global recursive
        recursive += 1

        return fib(n - 1) + fib(n - 2)

fib(n)
print(recursive, n - 2)