# source : https://www.acmicpc.net/problem/2997

# input
sequence = sorted(list(map(int, input().split())))

diff = min(sequence[1] - sequence[0], sequence[2] - sequence[1])
num = sequence[0]

for _ in range(4):
    num += diff

    if num not in sequence:
        print(num)
        break