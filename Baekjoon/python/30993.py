# source : https://www.acmicpc.net/problem/30993

from math import factorial

def main():
    # input
    n, a, b, c = map(int, input().split())
    
    print(factorial(n) // (factorial(a) * factorial(b) * factorial(c)))

if __name__ == '__main__':
    main()