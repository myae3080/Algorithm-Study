# source : https://www.acmicpc.net/problem/10214

# input
for _ in range(int(input())):
    y_scores, k_scores = 0, 0
    
    for __ in range(9):
        # input
        y, k = map(int, input().split())
        
        y_scores += y
        k_scores += k
    
    if y_scores > k_scores:
        print("Yonsei")
    elif y_scores < k_scores:
        print("Korea")
    else:
        print("Draw")