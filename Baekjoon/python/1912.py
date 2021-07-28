# dp

# input
n = int(input())
dp_list = [0] * n
seq_list = list(map(int, input().split()))

dp_list[0] = seq_list[0]

for i in range(1, n):
    dp_list[i] = max(seq_list[i], dp_list[i - 1] + seq_list[i])

print(max(dp_list))