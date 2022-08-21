# source : https://www.acmicpc.net/problem/1940

# input
n, m = int(input()), int(input())
materials = list(map(int, input().split()))

start, end = 0, n - 1
result = 0
materials.sort()

while start < end:
    armor = materials[start] + materials[end]
    
    if armor == m:
        result += 1
        start += 1
    elif armor < m:
        start += 1
    else:
        end -= 1

print(result)