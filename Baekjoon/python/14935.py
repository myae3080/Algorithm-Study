# source : https://www.acmicpc.net/problem/14935

# input
x = int(input())

def f(num: int) -> str:
    f_result = (num // (10 ** (len(str(num)) - 1))) * len(str(num))
    
    if num == f_result:
        return 'FA'
    else:
        return f(f_result)
    
print(f(x))