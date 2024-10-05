# source : https://www.acmicpc.net/problem/11971

import sys
input = sys.stdin.readline

def main():
    # input
    n, m = map(int, input().split())

    d1 = 1
    limits = [0] * 101
    for _ in range(n):
        # input
        road, limit = map(int, input().split())
        
        for i in range(d1, d1 + road):
            limits[i] = limit
        
        d1 += road
    
    d2 = 1
    speeds = [0] * 101
    for _ in range(m):
        # input
        road, speed = map(int, input().split())
        
        for i in range(d2, d2 + road):
            speeds[i] = speed
        
        d2 += road
    
    result = 0
    for i in range(1, 101):
        result = max(result, speeds[i] - limits[i])
    
    print(result)

if __name__ == '__main__':
    main()