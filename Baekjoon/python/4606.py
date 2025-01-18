# source : https://www.acmicpc.net/problem/4606

import sys
input = sys.stdin.readline

def main():
    encoding = {
        '%': '%25'
        , ' ': '%20'
        , '!': '%21'
        , '$': '%24'
        , '(': '%28'
        , ')': '%29'
        , '*': '%2a'
    }
    
    while 1:
        # input
        sentence = input().rstrip()
        
        if sentence == '#':
            break
        
        for key in encoding.keys():
            sentence = sentence.replace(key, encoding[key])
        
        print(sentence)

if __name__ == '__main__':
    main()