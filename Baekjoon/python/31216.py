# source : https://www.acmicpc.net/problem/31216

import sys
input = sys.stdin.readline

def main():
    size = 500000
    
    # Sieve of Erathsthenes
    sieve = [True] * size
    sieve[0], sieve[1] = False, False
    for i in range(2, int(size ** 0.5) + 1):
        if sieve[i]:           
            for j in range(i + i, size, i): 
                sieve[j] = False

    # 첫 번째 값 의미 없는 수로 할당
    super_primes = [0]
    count = 0
    for i in range(size):
        if sieve[i]:
            count += 1
            
            if sieve[count]:
                super_primes.append(i)

    # input
    for _ in range(int(input())):
        # input
        n = int(input())
        
        print(super_primes[n])

if __name__ == '__main__':
    main()