# source : https://www.acmicpc.net/problem/9612

import sys

input = sys.stdin.readline

def main():
    count_by_word = {}
    
    # input
    for _ in range(int(input())):
        # input
        word = input().rstrip()

        if word in count_by_word:
            count_by_word[word] += 1
        else:
            count_by_word[word] = 1
    
    result, count = '', 0
    for w, cnt in count_by_word.items():
        if cnt >= count:
            count = cnt

            if w > result:
                result = w
    
    print(result, count)

if __name__ == '__main__':
    main()