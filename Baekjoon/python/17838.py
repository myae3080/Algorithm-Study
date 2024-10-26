# source : https://www.acmicpc.net/problem/17838

import sys
input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        command = input().rstrip()
        
        if len(command) != 7:
            print(0)
            continue
        
        if not (command[0] == command[1] == command[4]):
            print(0)
            continue
        
        if not (command[2] == command[3] == command[5] == command[6]):
            print(0)
            continue
        
        if command[0] == command[2]:
            print(0)
            continue
        
        print(1)

if __name__ == '__main__':
    main()