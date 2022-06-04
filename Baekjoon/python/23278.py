# source : https://www.acmicpc.net/problem/23278

# input
n, l, h = map(int, input().split())
scores = sorted(list(map(int, input().split())))

print(sum(scores[l:len(scores) - h]) / (len(scores) - l - h))