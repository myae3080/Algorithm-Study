# source : https://www.acmicpc.net/problem/10539

# input
n = int(input())
sequence = list(map(int, input().split()))

result = []

for i, e in enumerate(sequence):
    if i == 0:
        result.append(sequence[i] * (i + 1))
    else:
        result.append((sequence[i] * (i + 1)) - sum(result[:i]))

result = [str(n) for n in result]
print(' '.join(result))