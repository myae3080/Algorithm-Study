# source : https://www.acmicpc.net/problem/9296

import sys
input = sys.stdin.readline

def main():
    # input
    for i in range(int(input())):
        # input
        n = int(input())
        exam, answer = input(), input()
        
        result = 0
        for j in range(n):
            if exam[j] != answer[j]:
                result += 1

        print('Case %d: %d' % (i + 1, result))

if __name__ == '__main__':
    main()