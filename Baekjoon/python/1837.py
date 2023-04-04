# source : https://www.acmicpc.net/problem/1837

def main():
    # input
    p, k = map(int, input().split())
    
    primes = getPrimes(k)
    is_good = True
    bad_prime = 0
    for prime in primes:
        if p % prime == 0:
            is_good = False
            bad_prime = prime
            break
    
    print('GOOD') if is_good else print('BAD', bad_prime)
    
def getPrimes(n: int) -> list:
    sieve = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == True:           
            for j in range(i + i, n, i): 
                sieve[j] = False
                
    return [i for i in range(2, n) if sieve[i]]

if __name__ == '__main__':
    main()