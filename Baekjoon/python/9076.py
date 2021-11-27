# source : https://www.acmicpc.net/problem/9076
# sorting

for _ in range(int(input())):
    # input
    scores = sorted(list(map(int, input().split())))
    
    if scores[3] - scores[1] >= 4:
        print("KIN")
    else:
        print(sum(scores[1:4]))