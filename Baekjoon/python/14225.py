# source : https://www.acmicpc.net/problem/14225

from itertools import combinations

def main():
    # input
    N = int(input())
    S = list(map(int, input().split()))

    result = [1] + [0] * 2000000
    for i in range(1, N + 1):
        for c in combinations(S, i):
            s = sum(c)
            if result[s] == 0:
                result[s] = 1
    
    print(result.index(0))

if __name__ == '__main__':
    main()