# source : https://www.acmicpc.net/problem/8979
# 100점

import sys
input = sys.stdin.readline

def main():
    # input
    n, k = map(int, input().split())

    medals = []
    for _ in range(n):
        # input
        medal = list(map(int, input().split()))

        medals.append(medal)
        if medal[0] == k:
            target = medal[1:]

    medals.sort(key=lambda c: (c[1], c[2], c[3]), reverse=True)

    for i in range(n):
        if medals[i][1:] == target:
            print(i + 1)
            break
        
if __name__ == '__main__':
    main()