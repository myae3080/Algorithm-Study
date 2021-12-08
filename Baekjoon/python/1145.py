# source : https://www.acmicpc.net/problem/1145
# brute forcing

# input
nums = list(map(int, input().split()))

min_num = min(nums)

while True:
    cnt = 0
    
    for i in nums:
        if min_num % i == 0:
            cnt += 1
    
    if cnt > 2:
        print(min_num)
        break

    min_num += 1