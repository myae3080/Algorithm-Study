# source : https://www.acmicpc.net/problem/20674

import sys
input = sys.stdin.readline

def main():
    result = 0
    min_num = 0
    
    # input
    for i in range(int(input())):
        # input
        num = int(input())
        
        if i == 0:
            min_num = num
        else:
            if num > min_num:
                result += (num - min_num)
            
            min_num = min(num, min_num)
    
    print(result)

if __name__ == '__main__':
    main()