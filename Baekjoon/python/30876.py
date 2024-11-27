# source : https://www.acmicpc.net/problem/30876

import sys
input = sys.stdin.readline

def main():
    result_x, result_y = 1001, 1001
    
    # input
    for _ in range(int(input())):
        # input
        x, y = map(int, input().split())
        
        if result_y > y:
            result_x = x
            result_y = y
    
    print(result_x, result_y)

if __name__ == '__main__':
    main()