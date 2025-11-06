# source : https://www.acmicpc.net/problem/3986

import sys

input = sys.stdin.readline

def main():
    result = 0

    # input
    for _ in range(int(input())):
        # input
        word = input().rstrip()

        if len(word) % 2 == 1:
            continue

        if word in ['AB', 'BA']:
            continue

        stack = []
        for c in word:
            if stack:
                if c == stack[-1]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        if not stack:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()