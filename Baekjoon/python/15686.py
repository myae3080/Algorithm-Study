# source : https://www.acmicpc.net/problem/15686

import sys
from itertools import combinations

input = sys.stdin.readline

def main():
    # input
    N, M = map(int, input().split())
    
    house, chicken = [], []
    for i in range(N):
        # input
        city_info = list(map(int, input().split()))
        
        for j in range(N):
            if city_info[j] == 1:
                house.append((i, j))
            elif city_info[j] == 2:
                chicken.append((i, j))
    
    results = []
    for m_chicken in combinations(chicken, M):
        total_min_chicken = 0
        for h in house:
            min_chicken = 1000
            
            for chi in m_chicken:
                min_chicken = min(min_chicken, abs(h[0] - chi[0]) + abs(h[1] - chi[1]))
            
            total_min_chicken += min_chicken
        
        results.append(total_min_chicken)
    
    print(min(results))

if __name__ == '__main__':
    main()