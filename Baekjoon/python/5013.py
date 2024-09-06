# source : https://www.acmicpc.net/problem/5013

import sys
input = sys.stdin.readline

def main():
    # input
    n = int(input())
    
    result = 0
    for _ in range(n):
        # input
        battle = input()
        
        is_win = True
        for i in range(1, len(battle)):
            if battle[i - 1] == 'C' and battle[i] == 'D':
                is_win = False
                break
        
        if is_win:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()