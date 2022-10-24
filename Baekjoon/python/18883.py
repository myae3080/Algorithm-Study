# source : https://www.acmicpc.net/problem/18883

# input
n, m = map(int, input().split())

number = 1
for i in range(n):
    nums = []
    for j in range(m):
        nums.append(str(number))
        number += 1
    
    print(' '.join(nums))