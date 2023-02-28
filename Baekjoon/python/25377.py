# source : https://www.acmicpc.net/problem/25377

import sys

def main():
    # input
    n = int(input())
    
    max_num = sys.maxsize
    answer = max_num
    for _ in range(n):
        # input
        a, b = map(int, input().split())
        
        if b >= a:
            answer = min(answer, b)
            
    print(-1) if answer == max_num else print(answer)
            
if __name__ == '__main__':
    main()