# source : https://www.acmicpc.net/problem/4436

import sys

input = sys.stdin.readline

def main():
    while 1:
        try:
            # input
            n = int(input())
        except:
            break
        
        num = [0] * 10
        result, rest = 0, 10
        curr_num = 0
        while rest > 0:
            result += 1
            curr_num += n
            
            for s in str(curr_num):
                if not num[int(s)]:
                    num[int(s)] = 1
                    rest -= 1
        
        print(result)

if __name__ == '__main__':
    main()