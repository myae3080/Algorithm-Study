# source : https://www.acmicpc.net/problem/2875
# math

# input
w, m, k = map(int, input().split())

team = 0

while 1:
    if w < 2 or m < 1 or (w + m) < k + 3:
        break
    
    w -= 2
    m -= 1
    team += 1

print(team)