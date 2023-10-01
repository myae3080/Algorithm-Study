# source : https://www.acmicpc.net/problem/1735

import math

def main():
    # input
    c1, p1 = map(int, input().split())
    c2, p2 = map(int, input().split())

    c = c1 * p2 + c2 * p1
    p = p1 * p2 

    gcd = math.gcd(c, p)

    print(c // gcd, p // gcd)

if __name__ == '__main__':
    main()