# source : https://www.acmicpc.net/problem/21567
# math

num_list = [0] * 10

# input
target = str(int(input()) * int(input()) * int(input()))

for s in target:
    num_list[int(s)] += 1

[print(n) for n in num_list]