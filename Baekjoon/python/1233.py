# source : https://www.acmicpc.net/problem/1233

# input
s1, s2, s3 = map(int, input().split())

nums = {}

for i in range(1, s1 + 1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            num = i + j + k
            
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1

for k, v in nums.items():
    if v == max(nums.values()):
        print(k)
        break