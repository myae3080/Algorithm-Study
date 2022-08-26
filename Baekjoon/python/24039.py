# source : https://www.acmicpc.net/problem/24039

primes, specials = [], []

def isPrimeNum(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True

for i in range(2, 105):
    if isPrimeNum(i):
        primes.append(i)
        
specials = [primes[i] * primes[i + 1] for i in range(len(primes) - 1)]

# input
n = int(input())

for num in specials:
    if num > n:
        print(num)
        break