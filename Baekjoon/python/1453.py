# source : https://www.acmicpc.net/problem/1453

dict = {}
count = 0

# input
num = int(input())
for i in list(map(int, input().split())):
    if i in dict:
        count += 1
    else:
        dict[i] = 1

print(count)