# source : https://www.acmicpc.net/problem/9358

import sys

input = sys.stdin.readline

def main():
    # input
    for i in range(int(input())):
        # input
        N = int(input())
        seq = list(map(int, input().split()))

        while len(seq) > 2:
            curr_seq = []
            for j in range(len(seq) // 2 + 1):
                curr_seq.append(seq[j] + seq[len(seq) - j - 1])
            
            seq = curr_seq

        print('Case #%d: %s' % (i + 1, 'Alice' if seq[0] > seq[-1] else 'Bob'))

if __name__ == '__main__':
    main()