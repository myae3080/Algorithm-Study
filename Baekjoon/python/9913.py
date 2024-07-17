# source : https://www.acmicpc.net/problem/9913

import sys
input = sys.stdin.readline

def main():
    frequency_by_num = {}
    
    # input
    for _ in range(int(input())):
        # input
        num = int(input())
        
        if num in frequency_by_num:
            frequency_by_num[num] += 1
        else:
            frequency_by_num[num] = 1
    
    print(max(frequency_by_num.values()))

if __name__ == '__main__':
    main()