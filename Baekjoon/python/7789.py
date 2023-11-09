# source : https://www.acmicpc.net/problem/7789

def main():
    # input
    origin, add = input().split()
    
    n1 = int(origin)
    n2 = int(add + origin)
    sieve = [True] * (n2 + 1)
    
    for i in range(2, int(n2 ** 0.5) + 1):
        if sieve[i]:
            for j in range(i + i, n2 + 1, i):
                sieve[j] = False
    
    print('Yes' if sieve[n1] and sieve[n2] else 'No')

if __name__ == '__main__':
    main()