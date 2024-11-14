# source : https://www.acmicpc.net/problem/3486

import sys
input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        a, b = input().split()
        
        new_num_sum = str(getNewNum(a) + getNewNum(b))
        
        print(getNewNum(new_num_sum))

def getNewNum(strNum: str) -> int:
    str_num_list = list(strNum)
    while 1:
        if str_num_list[-1] != '0':
            return int(''.join(str_num_list)[::-1])
        else:
            del str_num_list[-1]

if __name__ == '__main__':
    main()