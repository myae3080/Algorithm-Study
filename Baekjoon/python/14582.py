# source : https://www.acmicpc.net/problem/14582

# input
uj, sg = list(map(int, input().split())), list(map(int, input().split()))

uj_score, sg_score = 0, 0
is_reverse = False

for i in range(len(uj)):
    uj_score += uj[i]
    
    if uj_score > sg_score:
        is_reverse = True
        
    sg_score += sg[i]
        
print("Yes") if is_reverse else print("No")