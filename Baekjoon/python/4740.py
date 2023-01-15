# source : https://www.acmicpc.net/problem/4740

while 1:
    # input
    sentence = input()
    
    if sentence == '***':
        break
    
    print(sentence[::-1])