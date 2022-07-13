# source : https://www.acmicpc.net/problem/1075
# brute force

# input
n = int(input())
f = int(input())

front = (n // 100) * 100 

for num in range(front, front + 100):
    if num % f == 0:
        print(str(num)[-2:])
        break