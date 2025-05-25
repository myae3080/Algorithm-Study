# source : https://www.acmicpc.net/problem/11502

import sys

input = sys.stdin.readline

def main():
    primes = []
    for n in range(2, 1000):
        if isPrime(n):
            primes.append(n)
    
    # input
    for _ in range(int(input())):
        # input
        K = int(input())
        
        result = getPrimeSumList(K, primes)
        
        if len(result) == 0:
            print(0)
        else:
            print(*result)
        
def isPrime(num: int) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True

def getPrimeSumList(num: int, primes: list) -> list:
    for a in primes:
            for b in primes:
                sum1 = a + b
                if sum1 < num and b >= a:
                    for c in primes:
                        if sum1 + c == num and c >= b:
                            return [a, b, c]
    
    return []

if __name__ == '__main__':
    main()