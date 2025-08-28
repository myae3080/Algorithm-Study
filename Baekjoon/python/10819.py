# source : https://www.acmicpc.net/problem/10819

from itertools import permutations

def main():
    # input
    N = int(input())
    arr = list(map(int, input().split()))

    result = 0
    for p in permutations(arr):
        curr_sum = 0
        for i in range(1, N):
            curr_sum += abs(p[i] - p[i - 1])
        
        result = max(result, curr_sum)
    
    print(result)

if __name__ == '__main__':
    main()