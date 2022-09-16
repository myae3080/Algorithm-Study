# source : https://www.acmicpc.net/problem/1592

# input
n, m, l = map(int, input().split())

peoples = [0] * n
ball = 1
count = 0

while True:
    i = ball - 1
    peoples[i] += 1
    
    if peoples[i] == m:
        print(count)
        break
    else:
        if peoples[i] // 2 == 0:
            ball = (ball + l) % n
        else:
            ball = (ball + n - l) % n
    
    count += 1