# source : https://www.acmicpc.net/problem/2003

# input
n, m = map(int, input().split())
nums = list(map(int, input().split()))

start, end = 0, 1
count = 0

while start <= end and end <= n:
    total = sum(nums[start:end])
    
    if total == m:
        count += 1
        start += 1
    elif total < m:
        end += 1
    else:
        start += 1

print(count)