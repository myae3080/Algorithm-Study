# source : https://www.acmicpc.net/problem/9237
# greedy, sorting

# input
n = int(input())
tree = [i + 2 + v for i, v in enumerate(sorted(list(map(int, input().split())), reverse=True))]

print(max(tree))