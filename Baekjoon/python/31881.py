# source : https://www.acmicpc.net/problem/31881

import sys

input = sys.stdin.readline

def main():
    # input
    N, Q = map(int, input().rstrip().split())
    
    coms = [0] * N
    non_infected = N
    for _ in range(Q):
        # input
        query = list(input().rstrip().split())
        
        if len(query) == 1:
            print(non_infected)
            continue
        
        com_num = int(query[1]) - 1
        if query[0] == '1':
            if coms[com_num] == 0:
                non_infected -= 1
                coms[com_num] = 1
        else:
            if coms[com_num] == 1:
                non_infected += 1
                coms[com_num] = 0

if __name__ == '__main__':
    main()