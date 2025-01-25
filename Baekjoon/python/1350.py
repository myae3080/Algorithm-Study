# source : https://www.acmicpc.net/problem/1350

from math import ceil 

def main():
    # input
    N = int(input())
    files = list(map(int, input().split()))
    cluster = int(input())
    
    result = 0
    for file in files:
        if file == 0:
            continue
        
        result += ceil(file / cluster) * cluster
    
    print(result)

if __name__ == '__main__':
    main()