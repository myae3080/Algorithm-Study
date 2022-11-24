# source : https://www.acmicpc.net/problem/5692

import sys

def factorial(n: int) -> int:
    result = 1
    for i in range(n, 0, -1):
        result *= i
        
    return result

while 1:
    # input
    num = sys.stdin.readline().rstrip()
    
    if num == '0':
        break
    
    result = 0
    for i in range(len(num)):
        result += (int(num[i]) * factorial(len(num) - i))

    print(result)