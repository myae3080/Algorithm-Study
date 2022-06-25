# source : https://www.acmicpc.net/problem/3711

for _ in range(int(input())):
    # input
    g = int(input())
    student_ids = [int(input()) for __ in range(g)]
    
    m = 1
    
    while True:
        counts = []
        
        for id in student_ids:
            rest = id % m
            
            if rest in counts:
                break
            else:
                counts.append(rest) 
        
        if len(counts) == g:
            print(m)
            break
        else:
            m += 1