# source : https://www.acmicpc.net/problem/11134
# math

for _ in range(int(input())):
    cookie, per_day = map(int, input().split())

    print(cookie // per_day) if cookie % per_day == 0 else print((cookie // per_day) + 1)