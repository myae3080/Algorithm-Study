# source : https://www.acmicpc.net/problem/8558

from math import factorial

def main():
    # input
    n = int(input())

    print(str(factorial(n))[-1])

if __name__ == '__main__':
    main()