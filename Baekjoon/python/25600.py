# source : https://www.acmicpc.net/problem/25600

import sys

input = sys.stdin.readline

def main():
    result = 0

    # input
    for _ in range(int(input())):
        # input
        a, d, g = map(int, input().split())

        multiply = 2 if a == d + g else 1
        
        result = max(result, (multiply * (a * (d + g))))
    
    print(result)

if __name__ == '__main__':
    main()