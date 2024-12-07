# source : https://www.acmicpc.net/problem/9286

import sys
input = sys.stdin.readline

def main():
    # input
    n = int(input())
    
    for i in range(1, n + 1):
        print('Case %d:' % i)
        
        # input
        for _ in range(int(input())):
            # input
            graduated = int(input())
            
            if 0 < graduated + 1 < 7:
                print(graduated + 1)

if __name__ == '__main__':
    main()