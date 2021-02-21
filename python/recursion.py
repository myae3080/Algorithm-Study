# 재귀 함수를 실무에서 사용할 때는 신중히 고민 필요
#     -> 디버깅
#     -> stack overflow
#     -> tail recursion을 사용하는 방안도 있음 (python에서 의미가 있나..?)

# Fibonacci
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# 실행 결과
print('fib : ', fib(7))

# 1부터 n 까지 숫자의 합
def triangle_num(n):
    if n == 1:
        return 1

    return triangle_num(n-1) + n

# 실행 결과
print('tri : ', triangle_num(10))

#  factorial
def factorial(n):
    if n == 1:
        return 1        
    
    return factorial(n-1) * n

# 실행 결과
print('factorial : ', factorial(5))
