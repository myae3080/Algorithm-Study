# brute force

# input
num, max_num = map(int, input().split())
num_list = list(map(int, input().split()))

length = len(num_list)
target_num_list = []

for i in range(length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            temp_num = num_list[i] + num_list[j] + num_list[k]

            if temp_num <= max_num:
                target_num_list.append(temp_num)

print(max(target_num_list))
