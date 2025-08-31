# source : https://www.acmicpc.net/problem/9417

import sys
from math import gcd

input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        # input
        nums = list(map(int, input().split()))

        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                result = max(result, gcd(nums[i], nums[j]))
        
        print(result)

if __name__ == '__main__':
    main()