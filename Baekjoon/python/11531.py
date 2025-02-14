# source : https://www.acmicpc.net/problem/11531

import sys
from collections import defaultdict

input = sys.stdin.readline

def main():
    solve, score = 0, 0
    wrong_by_problem = defaultdict(int)
    while 1:
        # input
        log = input().rstrip()
        
        if log == '-1':
            print(solve, score)
            break
        
        m, problem, result = log.split()
        if result == 'wrong':
            wrong_by_problem[problem] += 1
        else:
            solve += 1
            score += (int(m) + (wrong_by_problem[problem] * 20))

if __name__ == '__main__':
    main()