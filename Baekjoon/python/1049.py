# source : https://www.acmicpc.net/problem/1049

import sys

input = sys.stdin.readline

def main():
    # input
    N, M = map(int, input().split())
    strings = [list(map(int, input().split())) for _ in range(M)]
    
    min_packages = min([s[0] for s in strings])
    min_one_string = min([s[1] for s in strings])
    
    result = min(min_one_string * N, (N // 6) * min_packages + (N % 6) * min_one_string, ((N // 6) + 1) * min_packages)
    
    print(result)

if __name__ == '__main__':
    main()