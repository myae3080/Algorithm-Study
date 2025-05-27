# source : https://www.acmicpc.net/problem/11145

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        case = input().rstrip()
        
        try:
            num = int(case)
            
            if num >= 0:
                print(num)
            else:
                print('invalid input')
        except:
            print('invalid input')
            
            continue

if __name__ == '__main__':
    main()