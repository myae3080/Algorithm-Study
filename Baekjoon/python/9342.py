# source : https://www.acmicpc.net/problem/9342

import sys

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        chromosome = input().rstrip()

        no_dup = ''.join(dict.fromkeys(chromosome))
        if len(no_dup) < 3:
            print('Good')
        elif len(no_dup) == 3:
            if no_dup == 'AFC':
                print('Infected!')
            else:
                print('Good')
        else:
            if no_dup[1:4] == 'AFC':
                print('Infected!')
            else:
                print('Good')
            

if __name__ == '__main__':
    main()