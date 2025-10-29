# source : https://www.acmicpc.net/problem/33753

from math import ceil

def main():
    # input
    A, B, C = map(int, input().split())
    T = int(input())

    fee = 0
    if T <= 30:
        fee = A
    else:
        fee += A

        left_time = T - 30
        fee += ((ceil(left_time / B)) * C)
    
    print(fee)

if __name__ == '__main__':
    main()