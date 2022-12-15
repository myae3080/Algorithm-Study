# source : https://www.acmicpc.net/problem/2204

while 1:
    # input
    n = int(input())
    
    if n == 0:
        break
    
    words = sorted([input() for _ in range(n)], key = lambda word: word.lower())
    
    print(words[0])