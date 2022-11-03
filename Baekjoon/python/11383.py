# source : https://www.acmicpc.net/problem/11383

origins = []
doubled_images = []

# input
n, m = map(int, input().split())
[origins.append(input()) for _ in range(n)]
[doubled_images.append(input()) for _ in range(n)]

is_eyfa = True
for i in range(n):
    doubled = ''
    for c in origins[i]:
        doubled += c * 2
    
    if doubled != doubled_images[i]:
        is_eyfa = False
        break

print('Eyfa') if is_eyfa else print('Not Eyfa')