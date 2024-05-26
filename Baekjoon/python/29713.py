# source : https://www.acmicpc.net/problem/29713

from collections import defaultdict

def main():
    # input
    n = int(input())
    alphas = input()
    
    base = 'BRONZESILVER'
    count_by_alpha = defaultdict(int)
    for c in base:
        count_by_alpha[c] = 0
    
    for a in alphas:
        if a in count_by_alpha:
            count_by_alpha[a] += 1
    
    count_by_alpha['E'] //= 2
    count_by_alpha['R'] //= 2
    
    print(min(count_by_alpha.values()))

if __name__ == '__main__':
    main()