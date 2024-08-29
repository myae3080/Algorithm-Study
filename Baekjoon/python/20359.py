# source : https://www.acmicpc.net/problem/20359

def main():
    # input
    n = int(input())
    
    p = 0
    while n % 2 == 0:
        p += 1
        n //= 2
    
    print(n, p)

if __name__ == '__main__':
    main()