# source : https://www.acmicpc.net/problem/6830

import sys
input = sys.stdin.readline

def main():
    result, temp = '', 201
    try:
        while 1:
            # input
            city, t = input().split()
            
            if int(t) < temp:
                result = city
                temp = int(t)
    except:
        print(result)

if __name__ == '__main__':
    main()