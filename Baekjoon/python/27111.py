# source : https://www.acmicpc.net/problem/27111

import sys
input = sys.stdin.readline

def main():
    records = [0] * 200001
    result = 0
    
    # input
    for _ in range(int(input())):
        # input
        a, b = map(int, input().split())
        
        if b == 0:
            if records[a] == 1:
                records[a] = 0
            else:
                result += 1
        else:
            if records[a] == 0:
                records[a] = 1
            else:
                result += 1
    
    result += records.count(1)
    
    print(result)

if __name__ == '__main__':
    main()