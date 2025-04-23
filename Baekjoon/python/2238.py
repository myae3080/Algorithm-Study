# source : https://www.acmicpc.net/problem/2238

import sys

input = sys.stdin.readline

def main():
    # input
    U, N = map(int, input().split())
    
    people_infos = [[] for _ in range((U + 1))]
    counts = [0] * (U + 1)
    for _ in range(N):
        # input
        S, P = input().split()
        
        people_infos[int(P)].append(S)
        counts[int(P)] += 1
    
    result_price = counts.index(min(c for c in counts if c != 0))
    
    print(people_infos[result_price][0], result_price)

if __name__ == '__main__':
    main()