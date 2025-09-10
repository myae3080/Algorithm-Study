# source : https://www.acmicpc.net/problem/11117

import sys
import copy

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        alpha = [0] * 26
        
        # input
        s = input().rstrip()

        for c in s:
            alpha[ord(c) - 65] += 1
    
        # input
        for _ in range(int(input())):
            # input
            word = input().rstrip()

            curr_alpha = copy.deepcopy(alpha)
            is_possible = True
            for c in word:
                if curr_alpha[ord(c) - 65] == 0:
                    is_possible = False

                    break
                else:
                    curr_alpha[ord(c) - 65] -= 1
            
            print('YES' if is_possible else 'NO')

if __name__ == '__main__':
    main()