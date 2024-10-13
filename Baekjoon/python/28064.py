# source : https://www.acmicpc.net/problem/28064

import sys
input = sys.stdin.readline

def main():
    # input
    N = int(input())
    names = [input().rstrip() for _ in range(N)]
    
    result = 0
    for i in range(N):
        name1 = names[i]
        
        for j in range(i + 1, N):
            name2 = names[j]
            
            idx = 0
            min_idx = min(len(name1), len(name2))
            while idx < min_idx:
                idx += 1
                
                if name1[:idx] == name2[-idx:] or name2[:idx] == name1[-idx:]:
                    result += 1
                    break
    
    print(result)

if __name__ == '__main__':
    main()