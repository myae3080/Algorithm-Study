# source : https://www.acmicpc.net/problem/10801

# input
a_score = list(map(int, input().split()))
b_score = list(map(int, input().split()))

a, b = 0, 0

for i in range(len(a_score)):
    if a_score[i] > b_score[i]:
        a += 1
    elif a_score[i] < b_score[i]:
        b += 1

print('A') if a > b else print('B') if a < b else print('D')