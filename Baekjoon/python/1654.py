# source : https://www.acmicpc.net/problem/1654
# binary search

# input
k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]

start, end = 1, max(lans)
result = 0

while start <= end:
    mid = (start + end) // 2
    
    if sum([lan // mid for lan in lans]) < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
    
print(result)