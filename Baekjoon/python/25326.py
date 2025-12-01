# source : https://www.acmicpc.net/problem/25326

import sys

input = sys.stdin.readline

def main():
    # input
    n, m = map(int, input().split())

    stu_prefers = [input().split() for _ in range(n)]

    for _ in range(m):
        # input
        q = input().split()

        result = 0
        for prefer in stu_prefers:
            is_match = True
            for i in range(3):
                if q[i] == '-':
                    continue

                if q[i] != prefer[i]:
                    is_match = False

                    break
            
            if is_match:
                result += 1
        
        print(result)

if __name__ == '__main__':
    main()