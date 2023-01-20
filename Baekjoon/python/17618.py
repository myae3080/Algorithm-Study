# source : https://www.acmicpc.net/problem/17618

# PyPy3
# input
n = int(input())

result = 0
for i in range(1, n + 1):
    temp = i
    s = 0
    while temp:
        s += temp % 10
        temp //= 10
    
    if i % s == 0: 
        result += 1

print(result)