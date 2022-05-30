# source : https://www.acmicpc.net/problem/5533

# input
n = int(input())

first_scores = []
second_scores = []
third_scores = []

for _ in range(n):
    # input
    a, b, c = map(int, input().split())
    
    first_scores.append(a)
    second_scores.append(b)
    third_scores.append(c)
    
for i in range(n):
    result = 0
    
    if first_scores.count(first_scores[i]) == 1:
        result += first_scores[i]
        
    if second_scores.count(second_scores[i]) == 1:
        result += second_scores[i]
        
    if third_scores.count(third_scores[i]) == 1:
        result += third_scores[i]
        
    print(result)