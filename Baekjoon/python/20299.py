# source : https://www.acmicpc.net/problem/20299

import sys 
input = sys.stdin.readline

teams = []

# input
N, K, L = map(int, input().split())
[teams.append(list(map(int, input().split()))) for _ in range(N)]

qualified_team = 0
qualified_ratings = []
for team in teams:
    is_qualified = True
    
    if sum(team) < K:
        is_qualified = False
    
    if is_qualified:
        for rating in team:
            if rating < L:
                is_qualified = False
                break
    
        if is_qualified:
            qualified_team += 1
            qualified_ratings.extend(team)
        
print(qualified_team)
[print(rating, end=' ') for rating in qualified_ratings]