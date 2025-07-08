# source : https://www.acmicpc.net/problem/9699

import sys

input = sys.stdin.readline

def main():
    # input
    for i in range(1, int(input()) + 1):
        # input
        nums = list(map(int, input().split()))
        
        print('Case #%d: %d' % (i, max(nums)))

if __name__ == '__main__':
    main()