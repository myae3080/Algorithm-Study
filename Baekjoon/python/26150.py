# source : https://www.acmicpc.net/problem/26150

import sys

input = sys.stdin.readline

def main():
    # input
    words_info = sorted([input().split() for _ in range(int(input()))], key=lambda li: int(li[1]))
    
    result = ''
    for info in words_info:
        result += info[0][int(info[2]) - 1]
    
    print(result.upper())
    

if __name__ == '__main__':
    main()