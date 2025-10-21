# source : https://www.acmicpc.net/problem/1392

import sys

input = sys.stdin.readline

def main():
    # input
    N, Q = map(int, input().split())
    notes = [int(input()) for _ in range(N)]
    times = [int(input()) for _ in range(Q)]

    for time in times:
        total_time = 0
        for i in range(N):
            total_time += notes[i]

            if total_time > time:
                print(i + 1)

                break

if __name__ == '__main__':
    main()