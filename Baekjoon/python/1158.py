# data structure, queue

# input
n, k = map(int, input().split())

josephus = [i for i in range(1, n + 1)]
result = []
idx = k - 1

while josephus:
    if idx >= len(josephus):
        idx %= len(josephus)

    result.append(josephus.pop(idx))

    # index 조정
    idx = idx - 1 + k

print(str(result).replace('[', '<').replace(']', '>'))