# source : https://www.acmicpc.net/problem/16693

from math import pi

def main():
    # input
    a, p1 = map(int, input().split())
    r, p2 = map(int, input().split())
    
    print('Whole pizza') if (p1 / a) > (p2 / (r ** 2 * pi)) else print('Slice of pizza')
        
if __name__ == '__main__':
    main()