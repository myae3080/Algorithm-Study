# source : https://www.acmicpc.net/problem/21983

from math import sqrt

def main():
    # input
    s = int(input())

    a = sqrt((2 * s) / (3 * sqrt(3)))
    perimeter = 6 * a
    
    print('%.8f' % perimeter)

if __name__ == '__main__':
    main()