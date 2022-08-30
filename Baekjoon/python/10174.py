# source : https://www.acmicpc.net/problem/10174

for _ in range(int(input())):
    # input
    word = input()
    
    word = word.lower()
    length = len(word)
    half = length // 2
    is_palindrome = True
    
    for i in range(half):
        if word[i] != word[length - i - 1]:
            is_palindrome = False
            break
    
    print('Yes') if is_palindrome else print('No')