# source : https://www.acmicpc.net/problem/7598

import sys

input = sys.stdin.readline

def main():
    while 1:
        # input
        flight, total = input().split()

        if flight == '#':
            break

        total = int(total)
        while 1:
            # input
            alpha, count = input().split()

            if alpha == 'X':
                break

            count = int(count)
            if alpha == 'B' and total + count <= 68:
                total += count
            elif alpha == 'C' and total - count >= 0:
                total -= count
        
        print(flight, total)

if __name__ == '__main__':
    main()