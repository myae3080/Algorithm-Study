# dp

# input
n = int(input())
dp_list = [0] * (n + 1)
pack_list = list(map(int, input().split()))

for i in range(1, n + 1):
    for j in range(i):
        dp_list[i] = max(dp_list[i], dp_list[i - j - 1] + pack_list[j])

print(dp_list[n])