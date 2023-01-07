# source : https://www.acmicpc.net/problem/2635

# input
n = int(input())

result = []
for i in range(n // 2, n + 1):
    nums = [n, i]
    
    j = 1
    while 1:
        if nums[j - 1] >= nums[j]:
            nums.append(nums[j - 1] - nums[j])
            j += 1
        else:
            break
    
    if len(nums) > len(result):
        result = nums 
    
print(len(result))
print(' '.join([str(num) for num in result]))