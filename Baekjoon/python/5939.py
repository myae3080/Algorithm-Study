# source : https://www.acmicpc.net/problem/5939

import sys
input = sys.stdin.readline

def main():
    # input
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]
    
    times.sort(key=lambda time: (time[0], time[1], time[2]))
    
    for time in times:
        print(*time)

if __name__ == '__main__':
    main()