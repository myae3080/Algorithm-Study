# data structure, queue

# input
n, k = map(int, input().split())
num_list = [n for n in range(1, n + 1)]

index = k - 1
result_list = []

while len(num_list) > 0:
    target_num = num_list[index]

    result_list.append(target_num)
    num_list.remove(target_num)

    if len(num_list) != 0:
        index = (index - 1 + k) % len(num_list)

print(str(result_list).replace('[', '<').replace(']', '>'))