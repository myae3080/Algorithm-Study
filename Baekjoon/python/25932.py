# source : https://www.acmicpc.net/problem/25932

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        nums_input = input().rstrip()
        
        print(nums_input)
        if '17' in nums_input and '18' in nums_input:
            print('both')
        elif '17' in nums_input:
            print('zack')
        elif '18' in nums_input:
            print('mack')
        else:
            print('none')
        print()

if __name__ == '__main__':
    main()