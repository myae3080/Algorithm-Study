# source : https://www.acmicpc.net/problem/21866

# input
scores = list(map(int, input().split()))

perfect_scores = [100, 100, 200, 200, 300, 300, 400, 400, 500]

if sum(scores) >= 100:
    is_not_hacker = True
    for i in range(len(scores)):    
        if scores[i] > perfect_scores[i]:
            print('hacker')
            is_not_hacker = False
            break
        
    if is_not_hacker:
        print('draw')
else:
    print('none')