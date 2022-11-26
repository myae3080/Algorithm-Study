# source : https://www.acmicpc.net/problem/15667

# input
count = int(input()) - 1

for k in range(1, count + 1):
    if k + (k ** 2) == count:
        print(k)
        break