# source : https://www.acmicpc.net/problem/12840

import sys

input = sys.stdin.readline

def main():
    # input
    h, m, s = map(int, input().split())
    
    seconds = h * 3600 + m * 60 + s
    
    # input
    for _ in range(int(input())):
        # input
        input_list = list(map(int, input().split()))
        
        if input_list[0] == 3:
            seconds %= (24 * 3600)
            
            h = seconds // 3600
            m = (seconds % 3600) // 60
            s = seconds % 3600 % 60
            
            print(h, m, s)
        else:
            if input_list[0] == 1:
                seconds += input_list[1]
            else:
                seconds -= input_list[1]

if __name__ == '__main__':
    main()