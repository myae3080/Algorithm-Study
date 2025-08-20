# source : https://www.acmicpc.net/problem/4758

import sys

input = sys.stdin.readline

def main():
    while 1:
        # input
        speed, weight, strength = map(float, input().split())

        if speed == weight == strength == 0:
            break

        result = []
        if speed <= 4.5 and weight >= 150 and strength >= 200:
            result.append('Wide Receiver')
        
        if speed <= 6.0 and weight >= 300 and strength >= 500:
            result.append('Lineman')
        
        if speed <= 5.0 and weight >= 200 and strength >= 300:
            result.append('Quarterback')
        
        print(' '.join(result) if len(result) != 0 else 'No positions')

if __name__ == '__main__':
    main()