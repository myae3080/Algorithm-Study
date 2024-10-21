# source : https://www.acmicpc.net/problem/18245

import sys
input = sys.stdin.readline

def main():
    line = 2
    
    while 1:
        # input
        password = input().rstrip()
        
        if password == 'Was it a cat I saw?':
            break
        
        for i in range(0, len(password), line):
            print(password[i], end='')
        
        print()
        
        line += 1

if __name__ == '__main__':
    main()