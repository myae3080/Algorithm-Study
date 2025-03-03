# source : https://www.acmicpc.net/problem/10546

import sys

input = sys.stdin.readline

def main():
    # input
    N = int(input())
    
    result_by_name = {}
    for _ in range(N):
        # input
        participant = input().rstrip()
        
        if participant in result_by_name:
            result_by_name[participant] += 1
        else:
            result_by_name[participant] = 1
    
    for _ in range(N - 1):
        # input
        finish = input().rstrip()
        
        if result_by_name[finish] == 1:
            del result_by_name[finish]
        else:
            result_by_name[finish] -= 1
    
    print(*result_by_name.keys())


if __name__ == '__main__':
    main()