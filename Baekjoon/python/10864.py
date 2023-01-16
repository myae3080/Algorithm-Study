# source : https://www.acmicpc.net/problem/10864

# input
n, m = map(int, input().split())

friends = []
for _ in range(m):
    # input
    friends.extend(list(map(int, input().split())))
    
[print(friends.count(i)) for i in range(1, n + 1)]