# source : https://www.acmicpc.net/problem/4383

import sys

input = sys.stdin.readline

def main():
    while 1:
        try:
            # input
            arr = list(map(int, input().split()))

            check = [i for i in range(1, arr[0])]
            result = []
            for i in range(1, len(arr) - 1):
                val = abs(arr[i] - arr[i + 1])
                if val not in result:
                    result.append(val)
            
            if sorted(result) == check:
                print('Jolly')
            else:
                print('Not jolly')
        except:
            break

if __name__ == '__main__':
    main()