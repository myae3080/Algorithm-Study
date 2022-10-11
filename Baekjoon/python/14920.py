# source : https://www.acmicpc.net/problem/14920

# input
n = int(input())

count = 1
while 1:
    if n == 1:
        print(count)
        break
    
    if n % 2 == 0:
        n /= 2
    else:
        n = (3 * n) + 1
    
    count += 1