# source : https://www.acmicpc.net/problem/10409

# input
n, time = map(int, input().split())
times = list(map(int, input().split()))

count = 0
for t in times:
    if time < t:
        break
    else:
        count += 1
        time -= t

print(count)