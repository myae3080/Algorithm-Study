# source : https://www.acmicpc.net/problem/1476

# input
e, s, m = map(int, input().split())

year = 1
while True:
    if not (e - year) % 15 and not (s - year) % 28 and not (m - year) % 19:
        break
    year += 1
    
print(year)