# source : https://www.acmicpc.net/problem/21756

# 100점
# input
nums = [i + 1 for i in range(int(input()))]

while len(nums) > 1:
    nums = [nums[i] for i in range(len(nums)) if i % 2 == 1]

print(nums[0])