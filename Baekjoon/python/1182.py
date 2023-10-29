# source : https://www.acmicpc.net/problem/1182

from itertools import combinations

def main():
    # input
    n, s = map(int, input().split())
    set = list(map(int, input().split()))

    result = 0
    for i in range(1, n + 1):
        for subset in combinations(set, i):
            if sum(subset) == s:
                result += 1
    
    print(result)

if __name__ == '__main__':
    main()