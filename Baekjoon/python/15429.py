# source : https://www.acmicpc.net/problem/15429

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        group = list(map(int, input().split()))
        
        gnome_order = group[1]
        for i in range(2, group[0]):
            if group[i] != gnome_order + 1:
                print(i)
                
                break
            else:
                gnome_order += 1

if __name__ == '__main__':
    main()