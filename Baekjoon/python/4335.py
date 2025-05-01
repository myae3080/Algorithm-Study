# source : https://www.acmicpc.net/problem/4335

import sys

input = sys.stdin.readline

def main():
    min_num = 1
    max_num = 10
        
    while 1:
        # input
        num = int(input())
        
        if num == 0:
            break
        
        # input
        answer = input().rstrip()
        
        if answer == 'right on':
            print('Stan may be honest' if min_num <= num <= max_num else 'Stan is dishonest')
            
            min_num = 1
            max_num = 10
        elif answer == 'too high':
            max_num = min(max_num, num - 1)
        else:
            min_num = max(min_num, num + 1)

if __name__ == '__main__':
    main()