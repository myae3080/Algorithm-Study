# source : https://www.acmicpc.net/problem/6513

import sys

input = sys.stdin.readline

def main():
    # input
    L, N = map(int, input().split())
    
    irregular_word_by_plural = {}
    for _ in range(L):
        # input
        irregular_word, plural = input().rstrip().split()
        
        irregular_word_by_plural[irregular_word] = plural
    
    for _ in range(N):
        # input
        word = input().rstrip()
        
        if word in irregular_word_by_plural:
            print(irregular_word_by_plural[word])
        else:
            if word[-2] not in ['a', 'e', 'i', 'o', 'u'] and word[-1] == 'y':
                print(word[:-1] + 'ies')
            elif word[-1] in ['o', 's', 'x']:
                print(word + 'es')
            elif word[-2:] in ['ch', 'sh']:
                print(word + 'es')
            else:
                print(word + 's')

if __name__ == '__main__':
    main()