# source : https://www.acmicpc.net/problem/8979

# 40점
def solution1():
    import sys
    
    # input
    input = sys.stdin.readline
    n, k = map(int, input().split())
    countries = [list(map(int, input().split())) for _ in range(n)]

    ranks = {}
    for country in countries:
        score = country[1] * 3 + country[2] * 2 + country[3] * 1
        
        if score in ranks:
            ranks[score].append(country[0])
        else:
            ranks[score] = [country[0]]
        
    sorted_scores = sorted(ranks.keys(), reverse=True)

    rank = 1
    for score in sorted_scores:
        if k in ranks[score]:
            print(rank)
            break
        
        rank += len(ranks[score])
        
solution1()