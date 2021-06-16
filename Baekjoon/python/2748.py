# fibonacci, dp

# input
n = int(input())

result_list = [0] * (n + 1)
result_list[1] = 1

for i in range(2, n + 1):
    # 시간 제한으로 재귀로 풀면 안됨
    result_list[i] = result_list[i - 1] + result_list[i - 2]

print(result_list[n])