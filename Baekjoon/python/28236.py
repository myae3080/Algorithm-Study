# source : https://www.acmicpc.net/problem/28236

import sys
input = sys.stdin.readline

def main():
    # input
    n, m, k = map(int, input().split())
    
    class_info = []
    for c in range(k):
        # input
        row, column = map(int, input().split())
        
        class_info.append([c + 1, (row - 1) + (m - column)])
    
    print(sorted(class_info, key=lambda li : (li[1], li[0]))[0][0])

if __name__ == '__main__':
    main()