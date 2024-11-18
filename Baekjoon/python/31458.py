# source : https://www.acmicpc.net/problem/31458

import sys
input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        expression = input().rstrip()
        
        str_num = '1' if expression.count('1') == 1 else '0'
        a, b = expression.split(str_num)
        
        a_len, b_len = len(a), len(b)
        if a_len == 0 and b_len == 0:
            print(str_num)
        elif a_len > 0 and b_len == 0:
            if str_num == '1':
                print(0 if len(a) % 2 == 1 else 1)
            else:
                print(1 if len(a) % 2 == 1 else 0)
        elif a_len == 0 and b_len > 0:
            print(1)
        else:
            print(0 if len(a) % 2 == 1 else 1)

if __name__ == '__main__':
    main()