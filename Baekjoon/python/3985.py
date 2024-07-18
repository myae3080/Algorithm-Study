# source : https://www.acmicpc.net/problem/3985

import sys
input = sys.stdin.readline

def main():
    # input
    L = int(input())
    N = int(input())
    paper = [tuple(map(int, input().split())) for _ in range(N)]
    
    # cake numbering
    cakes = [0] * (L + 1)
    for i in range(N):
        for j in range(paper[i][0], paper[i][1] + 1):
            if cakes[j] == 0: 
                cakes[j] = i + 1
    
    # expect
    expect = [p[1] - p[0] for p in paper]
    
    # actual
    actual_num, pieces = 0, 0
    for num in range(1, N + 1):
        count = cakes.count(num)
        
        if count > pieces:
            pieces = count
            actual_num = num
    
    print(expect.index(max(expect)) + 1)
    print(actual_num)
    

if __name__ == '__main__':
    main()