# source : https://www.acmicpc.net/problem/4631

import sys

input = sys.stdin.readline

def main():
    no = 1
    while 1:
        # input
        n = int(input())

        if n == 0:
            break

        # input
        names = [input().rstrip() for _ in range(n)]

        start, end = 0, n - 1
        is_start = True
        seq = []
        for _ in range(n):
            if is_start:
                seq.append(start)
                start += 1
            else:
                seq.append(end)
                end -= 1
            
            is_start = not is_start

        
        result = [''] * n
        for i in range(n):
            result[seq[i]] = names[i]

        print('SET %d' % no)
        for name in result:
            print(name)

        no += 1

if __name__ == '__main__':
    main()