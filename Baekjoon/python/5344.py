# source : https://www.acmicpc.net/problem/5344

import math

def main():
    # input
    for _ in range(int(input())):
        # input
        a, b = map(int, input().split())
        
        print(math.gcd(a, b))

if __name__ == '__main__':
    main()