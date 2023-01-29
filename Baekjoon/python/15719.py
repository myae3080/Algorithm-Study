# source : https://www.acmicpc.net/problem/15719

import sys

def main():
    # input
    n = int(input())
    s = sys.stdin.readline().rstrip()
    
    sum_num = sum([i for i in range(1, n)])
    sum_input = 0
    
    num = ''
    for c in s:
        if c.isdigit():
            num += c
        else:
            sum_input += int(num)
            num = ''
    sum_input += int(num)
            
    print(sum_input - sum_num)

if __name__ == '__main__':
    main()