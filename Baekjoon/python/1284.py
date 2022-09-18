# source : https://www.acmicpc.net/problem/1284

while True:
    # input
    N = input()

    if N == '0':
        break
    
    result = 1
    for n in N:
        result += 1
        if n == '0':
            result += 4
        elif n == '1':
            result += 2
        else:
            result += 3
    
    print(result)