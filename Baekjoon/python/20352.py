# source : https://www.acmicpc.net/problem/20352

from math import pi

def main():
    # input
    area = int(input())
    
    r = (area / pi) ** 0.5
    
    print(2 * pi * r)

if __name__ == '__main__':
    main()