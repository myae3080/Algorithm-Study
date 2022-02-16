# https://www.acmicpc.net/problem/5568

from itertools import combinations, permutations

# input
n = int(input())
k = int(input())
nums = [input() for _ in range(n)]

result = set()

[result.add(''.join(tu)) for tu in permutations(nums, k)]
    
print(len(result))