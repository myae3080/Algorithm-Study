# source : https://www.acmicpc.net/problem/26502

import sys
input = sys.stdin.readline

def main():
    decoder = {
        'y': 'a'
        , 'a': 'e'
        , 'e': 'i'
        , 'i': 'o'
        , 'o': 'u'
        , 'u': 'y'
    }
    
    # input
    for _ in range(int(input())):
        # input
        line = input().strip()
        
        result = ''
        for c in line:
            if c.lower() in decoder:
                result += decoder[c] if c.islower() else decoder[c.lower()].upper()
            else:
                result += c
        
        print(result)

if __name__ == '__main__':
    main()