# source : https://www.acmicpc.net/problem/20920

import sys
input = sys.stdin.readline

def main():
    # input
    n, m = map(int, input().split())
    
    words = {}
    for _ in range(n):
        # input
        word = input().rstrip()
        
        if len(word) >= m:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    for item in sorted(words.items(), key=lambda item: (-item[1], -len(item[0]), item[0])):
        print(item[0])

if __name__ == '__main__':
    main()