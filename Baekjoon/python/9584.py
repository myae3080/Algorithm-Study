# source : https://www.acmicpc.net/problem/9584

import sys

input = sys.stdin.readline

def main():
    # input
    input_code = input().rstrip()
    
    results = []
    for _ in range(int(input())):
        # input
        code = input().rstrip()
        
        for i in range(len(input_code)):
            is_correspond = True 
            if input_code[i] != '*':
                if input_code[i] != code[i]:
                    is_correspond = False
                    
                    break
            
        if is_correspond:
            results.append(code)
    
    print(len(results))
    for c in results:
        print(c)

if __name__ == '__main__':
    main()