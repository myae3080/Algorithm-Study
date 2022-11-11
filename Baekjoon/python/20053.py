# source : https://www.acmicpc.net/problem/20053

for _ in range(int(input())):
    # input
    n = int(input())
    nums = list(map(int, input().split()))
    
    print(min(nums), max(nums))