# source : https://www.acmicpc.net/problem/32342

import sys
input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        query = input()
        
        result = 0
        for i in range(len(query) - 2):
            if query[i:i + 3] == 'WOW':
                result += 1
        
        print(result)

if __name__ == '__main__':
    main()