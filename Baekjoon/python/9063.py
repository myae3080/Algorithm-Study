# source : https://www.acmicpc.net/problem/9063

import sys

def main():
    input = sys.stdin.readline
    x_pts, y_pts = [], []
    
    # input
    for _ in range(int(input())):
        # input
        x, y = map(int, input().split())

        x_pts.append(x)
        y_pts.append(y)
    
    print((max(x_pts) - min(x_pts)) * (max(y_pts) - min(y_pts)))

if __name__ == '__main__':
    main()