# source : https://www.acmicpc.net/problem/3778

import sys
input = sys.stdin.readline

def main():
    # input
    for i in range(1, int(input()) + 1):
        # input
        A, B = input().rstrip(), input().rstrip()
        
        a_ascii, b_ascii = [0] * 26, [0] * 26
        for j in range(len(A)):
            a_ascii[ord(A[j]) - 97] += 1
        for j in range(len(B)):
            b_ascii[ord(B[j]) - 97] += 1
        
        result = 0
        for j in range(26):
            result += abs(a_ascii[j] - b_ascii[j])
        
        print('Case #%d: %d' % (i, result))

if __name__ == '__main__':
    main()