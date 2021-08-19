# source : https://www.acmicpc.net/problem/1057
# math, brute force

# input
n, kim, im = map(int, input().split())

count = 0

while True:
    if kim == im:
        print(count)
        break
    else:
        kim -= kim // 2
        im -= im // 2
        count += 1