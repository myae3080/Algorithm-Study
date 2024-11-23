# source : https://www.acmicpc.net/problem/21212

import sys
input = sys.stdin.readline

def main():
    result = 10001
    
    # input
    for _ in range(int(input())):
        # input
        required, quantity = map(int, input().split())
        
        result = min(result, quantity // required)
    
    print(result)

if __name__ == '__main__':
    main()