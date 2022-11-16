# source : https://www.acmicpc.net/problem/14491

# input
T = int(input())

result = ''
while T:
    result += str(T % 9)
    T //= 9

print(result[::-1])