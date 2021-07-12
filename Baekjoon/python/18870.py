# sorting

# input
n = int(input())
num_list = list(map(int, input().split()))

num_dict = {}
result_list = []
count = 0

for n in sorted(num_list):
    if n not in num_dict:
        num_dict[n] = count
        count += 1

for n in num_list:
    result_list.append(num_dict[n])

print(str(result_list).replace('[', '').replace(']', '').replace(',', ''))