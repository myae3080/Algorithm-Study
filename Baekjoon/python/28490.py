# source : https://www.acmicpc.net/problem/28490

import sys
input = sys.stdin.readline

def main():
    results = []
    
    # input
    for _ in range(int(input())):
        # input
        w, h = map(int, input().split())
        
        results.append(w * h)
    
    print(max(results))

if __name__ == '__main__':
    main()