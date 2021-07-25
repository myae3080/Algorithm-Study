# math, string, number theory, prime number

num = 0
n = 1050
sieve = [True] * n

m = int(n ** 0.5)

for i in range(2, m + 1):
    if sieve[i] == True:           
        for j in range(i + i, n, i): 
            sieve[j] = False

# input
for s in input():
    ascii = ord(s)
    
    if ascii > 96 and ascii < 123:
        num += (ascii - 96)
    
    if ascii > 64 and ascii < 91:
        num += (ascii - 38)

print('It is a prime word.') if sieve[num] else print('It is not a prime word.')