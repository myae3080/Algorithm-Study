# source : https://www.acmicpc.net/problem/13221

import sys
input = sys.stdin.readline

def main():
    # input
    x, y = map(int, input().split())
    
    coordinate_by_distance = {}
    
    # input
    for _ in range(int(input())):
        # input
        a, b = map(int, input().split())
        
        coordinate_by_distance[abs(x - a) + abs(y - b)] = '%s %s' % (a, b)
    
    print(coordinate_by_distance[min(coordinate_by_distance)])

if __name__ == '__main__':
    main()