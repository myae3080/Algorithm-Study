# source : https://www.acmicpc.net/problem/30821

from math import factorial

def main():
    # input
    n = int(input())
    
    print(factorial(n) // (factorial(n - 5) * factorial(5)))

if __name__ == '__main__':
    main()