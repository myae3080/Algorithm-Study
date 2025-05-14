# source : https://www.acmicpc.net/problem/24408

import sys

input = sys.stdin.readline

def main():
    first_num = 0
    
    # input
    for _ in range(int(input())):
        # input
        num = int(input())
        
        if first_num == 0:
            first_num = num
        else:
            if num % first_num == 0:
                print(num)
                
                first_num = 0

if __name__ == '__main__':
    main()