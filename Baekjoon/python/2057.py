# source : https://www.acmicpc.net/problem/2057

from math import factorial

def main():
    factorials = [factorial(i) for i in range(21)]
    
    # input
    n = int(input())
    
    if n == 0:
        print('NO')
    else:
        for i in range(20, -1, -1):
            if n >= factorials[i]:
                n -= factorials[i]

        print('YES' if n == 0 else 'NO')

if __name__ == '__main__':
    main()