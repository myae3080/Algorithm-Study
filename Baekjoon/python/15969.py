# source : https://www.acmicpc.net/problem/15969
# math

# input
n = int(input())
numbers = list(map(int, input().split()))

print(max(numbers) - min(numbers))