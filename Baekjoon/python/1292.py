# math

# input
from_num, to_num = map(int, input().split())

# 수열 세팅
seq = []

for i in range(1, to_num + 1):
    for k in range(i):
        seq.append(i)

result = 0

for i in range(from_num, to_num + 1):
    result += seq[i - 1]

print(result)
