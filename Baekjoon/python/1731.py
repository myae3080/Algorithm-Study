# source : https://www.acmicpc.net/problem/1731

# input
sequence = [int(input()) for _ in range(int(input()))]

if sequence[1] - sequence[0] == sequence[2] - sequence[1]:
    print(sequence[-1] + sequence[1] - sequence[0])
else:
    print(sequence[-1] * (sequence[1] // sequence[0]))