# source : https://www.acmicpc.net/problem/14489

# input
total = sum(map(int, input().split()))
chicken = int(input())

print(total - 2 * chicken) if total >= 2 * chicken else print(total)