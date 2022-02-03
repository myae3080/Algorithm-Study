# https://www.acmicpc.net/problem/9506
# math, number theory

while True:
    # input
    n = int(input())
    
    if n == -1:
        break
    
    divisors = []
    
    for num in range(1, n):
        if n % num == 0:
            divisors.append(num)
    
    if n == sum(divisors):
        print(str(n) + " = " + ' + '.join(map(str, divisors)))
    else:
        print(str(n) + " is NOT perfect.")