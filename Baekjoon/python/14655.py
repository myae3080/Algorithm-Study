# source : https://www.acmicpc.net/problem/14655

# input
N = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

result = 0
for i in range(N):
    result += (abs(first[i]) + abs(second[i]))

print(result)