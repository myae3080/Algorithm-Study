# source : https://www.acmicpc.net/problem/26314

import sys
input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        word = input().rstrip()
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        vowel_cnt = 0
        for c in word:
            if c in vowels:
                vowel_cnt += 1
        
        print(word)
        print(1 if vowel_cnt > len(word) - vowel_cnt else 0)

if __name__ == '__main__':
    main()