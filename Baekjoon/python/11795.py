# source : https://www.acmicpc.net/problem/11795

import sys
input = sys.stdin.readline

def main():
    setA, setB, setC = 0, 0, 0
    
    # input
    for _ in range(int(input())):
        # input
        a, b, c = map(int, input().split())
        
        setA += a
        setB += b
        setC += c
        
        min_set = min(setA, setB, setC)
        if min_set >= 30:
            print(min_set)
            
            setA -= min_set
            setB -= min_set
            setC -= min_set
        else:
            print('NO')

if __name__ == '__main__':
    main()