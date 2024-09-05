# source : https://www.acmicpc.net/problem/6784

import sys
input = sys.stdin.readline

def main():
    # input
    N = int(input())
    questions = [input() for _ in range(N)]
    answers = [input() for _ in range(N)]
    
    result = 0
    for i in range(N):
        if questions[i] == answers[i]:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()