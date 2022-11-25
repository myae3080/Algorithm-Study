# source : https://www.acmicpc.net/problem/3029

# input
h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

start = h1 * 60 * 60 + m1 * 60 + s1
end = h2 * 60 * 60 + m2 * 60 + s2

result = 0
if end < start:
    result = 24 * 60 * 60
result += end - start

if result != 0:
    hh, mm, ss = result // 3600, result // 60 % 60, result % 60
else:
    hh, mm, ss = 24, 0, 0

print('%02d:%02d:%02d' % (hh, mm, ss))