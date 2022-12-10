# source : https://www.acmicpc.net/problem/16433

# input
N, R, C = map(int, input().split())

result = []
odd_field = ['v' if i % 2 == 1 else '.' for i in range(N)]
even_field = ['v' if i % 2 == 0 else '.' for i in range(N)]
if C % 2 == 1:
    if R % 2 == 1:
        for n in range(N):
            result.append(odd_field) if n % 2 == 1 else result.append(even_field)
    else:
        for n in range(N):
            result.append(odd_field) if n % 2 == 0 else result.append(even_field)
else:
    if R % 2 == 0:
        for n in range(N):
            result.append(odd_field) if n % 2 == 1 else result.append(even_field)
    else:
        for n in range(N):
            result.append(odd_field) if n % 2 == 0 else result.append(even_field)
    
[print(''.join(result[i])) for i in range(N)]