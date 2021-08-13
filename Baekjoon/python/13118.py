# source : https://www.acmicpc.net/problem/13118

# input
people = list(map(int, input().split()))
x, y, r = map(int, input().split())

if people.count(x) > 0:
    print(people.index(x) + 1)
else:
    print(0)