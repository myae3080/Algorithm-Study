# source : https://www.acmicpc.net/problem/30394

import sys
input = sys.stdin.readline

def main():
    y_vals = []
    
    # input
    for _ in range(int(input())):
        # input
        x, y = map(int, input().split())
        
        y_vals.append(y)
    
    print(max(y_vals) - min(y_vals))

if __name__ == '__main__':
    main()