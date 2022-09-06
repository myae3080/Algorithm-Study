# source : https://www.acmicpc.net/problem/15233

# input
a, b, g = map(int, input().split())
A, B = input().split(), input().split()
goals = {}
for s in input().split():
    if s in goals:
        goals[s] += 1
    else:
        goals[s] = 1

a_scores, b_scores = 0, 0
for name in A:
    if name in goals:
        a_scores += goals[name]

for name in B:
    if name in goals:
        b_scores += goals[name]

print('A') if a_scores > b_scores else print('TIE') if a_scores == b_scores else print('B')