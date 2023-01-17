# source : https://www.acmicpc.net/problem/23348

# input
score1, score2, score3 = map(int, input().split())
n = int(input())

result = 0
for i in range(n):
    scores = 0
    
    for j in range(3):
        # input
        level1, level2, level3 = map(int, input().split())
        
        scores += (level1 * score1) + (level2 * score2) + (level3 * score3)
    
    result = max(result, scores)

print(result)