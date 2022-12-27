# source : https://www.acmicpc.net/problem/5656

import sys
input = sys.stdin.readline

i = 1
while 1:
    # input
    a, operator, b = input().split()
    
    if operator == 'E':
        break
    
    isTrue = True
    num1, num2 = int(a), int(b)
    if operator == '>':
        isTrue = num1 > num2
    elif operator == '>=':
        isTrue = num1 >= num2
    elif operator == '<':
        isTrue = num1 < num2
    elif operator == '<=':
        isTrue = num1 <= num2
    elif operator == '==':
        isTrue = num1 == num2
    else:
        isTrue = num1 != num2
    
    print('Case {0}: {1}'.format(i, str(isTrue).lower()))
    
    i += 1