# source : https://www.acmicpc.net/problem/19751

from itertools import permutations
from sys import maxsize

def main():
    # input
    nums = list(map(int, input().split()))

    value = maxsize
    result = 0
    for p in permutations(nums, 4):
        curr_value = (p[0] / p[1]) + (p[2] / p[3])
        if curr_value < value:
            value = curr_value
            result = p
    
    print(*result)

if __name__ == '__main__':
    main()