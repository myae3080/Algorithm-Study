# source : https://www.acmicpc.net/problem/3047

# input
numbers = sorted(list(map(int, input().split())))

[print(numbers[ord(s) - 65], end=' ') for s in input()]