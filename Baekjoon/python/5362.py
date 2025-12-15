# source : https://www.acmicpc.net/problem/5362

import sys

input = sys.stdin.readline

def main():
    while 1:
        # input
        message = input().rstrip()

        if message == '':
            break

        print(message.replace('iiing', 'th'))

if __name__ == '__main__':
    main()