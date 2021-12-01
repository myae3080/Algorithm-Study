# source : https://www.acmicpc.net/problem/9728
# two pointer

for i in range(int(input())):
    # input
    total, target = map(int, input().split())
    nums = list(map(int, input().split()))
    
    count = 0
    start, end = 0, total - 1
    
    while start <= end:
        two_sum = nums[start] + nums[end]
    
        if two_sum > target:
            end -= 1
        elif two_sum < target:
            start += 1
        else:
            count += 1
            start += 1
    
    print("Case #" + str(i + 1) + ": " + str(count))