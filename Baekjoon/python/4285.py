# source : https://www.acmicpc.net/problem/4285

import sys

input = sys.stdin.readline

def main():
    while 1:
        # input
        input_str = input().strip()
        
        if input_str == '0':
            break

        # input
        k, m = map(int, input_str.split())
        classes = list(map(int, input().split()))

        is_valid = True
        for _ in range(m):
            # input
            pick = list(map(int, input().split()))

            if is_valid:
                c, r = pick[0], pick[1]

                for category in pick[2:]:
                    if category in classes:
                        r -= 1
                
                if r > 0:
                    is_valid = False
        
        print('yes' if is_valid else 'no')

if __name__ == '__main__':
    main()