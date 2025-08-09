# source : https://www.acmicpc.net/problem/2961

from itertools import combinations
import sys 

input = sys.stdin.readline

def main():
    # input
    N = int(input())
    dishes = [list(map(int, input().split())) for _ in range(N)]

    result = 1000000000
    for i in range(1, N + 1):
        for combination in list(combinations(dishes, i)):
            sour, bitter = 1, 0
            for dish in combination:
                sour *= dish[0]
                bitter += dish[1]
            
            result = min(result, abs(sour - bitter))
    
    print(result)

if __name__ == '__main__':
    main()