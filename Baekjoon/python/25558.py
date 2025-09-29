# source : https://www.acmicpc.net/problem/25558

import sys

input = sys.stdin.readline

def main():
    # input
    N = int(input())
    sx, sy, ex, ey = map(int, input().split())

    distances = []
    for _ in range(N):
        # input
        coordinates = [list(map(int, input().split())) for _ in range(int(input()))]

        prev_x, prev_y = sx, sy
        distance = 0
        for co in coordinates:
            distance += (abs(co[0] - prev_x) + abs(co[1] - prev_y))
            prev_x, prev_y = co[0], co[1]
        
        distance += (abs(ex - prev_x) + abs(ey - prev_y))
        distances.append(distance)
    
    print(distances.index(min(distances)) + 1)

if __name__ == '__main__':
    main()