# source : https://www.acmicpc.net/problem/1544

import sys

input = sys.stdin.readline

def main():
    # input
    N = int(input())
    words = [input().rstrip() for _ in range(N)]
    
    results = [words[0]]
    for w in words[1:]:
        compares = results
        is_same = False
        for compare in compares:
            if len(compare) == len(w):
                for i in range(len(w)):
                    if compare == w[i:] + w[:i]:
                        is_same = True

                        break
                
        if not is_same:
            results.append(w)
        
    print(len(results))

if __name__ == '__main__':
    main()