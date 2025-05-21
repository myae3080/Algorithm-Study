# source : https://www.acmicpc.net/problem/28278

import sys

input = sys.stdin.readline

def main():
    stack = []
    
    # input
    for _ in range(int(input())):
        # input
        inputs = list(map(int, input().split()))
        
        if inputs[0] == 1:
            stack.append(inputs[1])
        elif inputs[0] == 2:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        elif inputs[0] == 3:
            print(len(stack))
        elif inputs[0] == 4:
            print(1 if len(stack) == 0 else 0)
        else:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])

if __name__ == '__main__':
    main()