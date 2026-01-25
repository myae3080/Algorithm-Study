# source : https://www.acmicpc.net/problem/17254

import sys

input = sys.stdin.readline

def main():
    # input
    N, M = map(int, input().split())
    
    inputs = []
    for _ in range(M):
        # input
        a, b, c = input().split()

        inputs.append((int(a), int(b), c))
    
    inputs.sort(key = lambda i: (i[1], i[0]))

    print(''.join(i[-1] for i in inputs))

if __name__ == '__main__':
    main()