# source : https://www.acmicpc.net/problem/26511

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        word = input().rstrip()

        d = {}
        for c in word:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        
        if len(d) <= 2:
            print(0)

            continue

        print(sum(sorted(d.values())[:len(d) - 2]))

if __name__ == '__main__':
    main()