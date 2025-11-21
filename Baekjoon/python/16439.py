# source : https://www.acmicpc.net/problem/16439

from itertools import combinations

def main():
    # input
    N, M = map(int, input().split())
    preferences = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    chicken = [i for i in range(M)]
    for combi in combinations(chicken, 3):
        curr_max = 0
        for n in range(N):
            curr_max += max(preferences[n][combi[0]], preferences[n][combi[1]], preferences[n][combi[2]])
        
        result = max(result, curr_max)

    print(result)            

if __name__ == '__main__':
    main()