# source : https://www.acmicpc.net/problem/3595

# PyPy3

import sys

def main():
    # input
    n = int(input())
    
    min_abc = ''
    min_area = sys.maxsize
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a * b > n:
                break
            
            for c in range(1, n + 1):
                if a * b * c > n:
                    break
                else:
                    if a * b * c == n:
                        area = (a * b) * 2 + (b * c) * 2 + (c * a) * 2
                    
                        if area < min_area:
                            min_abc = '%d %d %d' % (a, b, c)
                            min_area = area
    
    print(min_abc)

if __name__ == '__main__':
    main()