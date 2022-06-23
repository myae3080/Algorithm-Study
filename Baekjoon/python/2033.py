# source : https://www.acmicpc.net/problem/2033

# input
n = int(input())

multiplier = 1

while True:
    digit = 10 **  multiplier
    
    if n > digit:
        if n % digit >= digit // 2:
            n += digit // 2
        n -= n % digit
        
        multiplier += 1
    else:
        break

print(n)