# source : https://www.acmicpc.net/problem/24820

import sys

input = sys.stdin.readline

def main():
    # input
    letters = input().rstrip()
    for _ in range(int(input())):
        # input
        word = input().rstrip()

        if letters[0] not in word:
            continue
        if len(word) < 4:
            continue

        is_valid = True
        for c in word:
            if c not in letters:
                is_valid = False

                break
        
        if is_valid:
            print(word)

if __name__ == '__main__':
    main()