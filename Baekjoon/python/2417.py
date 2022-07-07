# source : https://www.acmicpc.net/problem/2417
# math, binary search

# input
n = int(input())

start, end = 0, int((2 ** 63) ** 0.5)
result = 0

while start < end:
    mid = (start + end) // 2
    sq = mid ** 2
    
    if sq > n:
        end = mid - 1
    elif sq < n:
        start = mid + 1
    else:
        result = mid
        break

if result == 0:
    if end ** 2 < n:
        result = end + 1     
    else: 
        result = end

print(result)