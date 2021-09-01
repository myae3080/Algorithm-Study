# source : https://www.acmicpc.net/problem/2460
# math

passenger = [0] * 10
num = 0

# input
for n in range(10):
    o, i = map(int, input().split())

    num += (i - o)
    passenger[n] = num

print(max(passenger))