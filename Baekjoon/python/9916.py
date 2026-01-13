# source : https://www.acmicpc.net/problem/9916

from math import factorial

def main():
    # input
    n = int(input())

    print(str(factorial(n)).count('0'))

if __name__ == '__main__':
    main()