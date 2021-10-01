# source : https://www.acmicpc.net/problem/11948
# math

a, b = [], []

# input
for i in range(6):
    if i < 4:
        a.append(int(input()))
    else:
        b.append(int(input()))

print(sum(sorted(a)[1:]) + max(b))