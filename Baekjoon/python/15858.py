# source : https://www.acmicpc.net/problem/15858

from decimal import Decimal

def main():
    # input
    a, b, c = map(int, input().split())
    
    print(Decimal(a) * Decimal(b) / Decimal(c))

if __name__ == '__main__':
    main()