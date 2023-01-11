# source : https://www.acmicpc.net/problem/5648

line_num, total = 0, 0
result = []

while 1:
    # input
    nums = input().split()
    
    if not line_num:
        total = int(nums[0])
        nums = nums[1:]
    
    for num in nums:
        result.append(int(''.join(reversed(num)).lstrip('0')))
        line_num += 1
    
    if line_num == total:
        break
    
[print(num) for num in sorted(result)]