# source : https://www.acmicpc.net/problem/33557

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        a, b = input().rstrip().split()
        
        normal = int(a) * int(b)
        
        if len(a) > len(b):
            b = '1' * (len(a) - len(b)) + b
        elif len(b) > len(a):
            a = '1' * (len(b) - len(a)) + a
            
        wierd = ''
        for i in range(max(len(a), len(b))):
            wierd += str(int(a[i]) * int(b[i]))
        
        if int(wierd) == normal:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    main()