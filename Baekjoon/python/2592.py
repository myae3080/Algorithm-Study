# source : https://www.acmicpc.net/problem/2592
# math

num_dict = dict()
total = 0

for _ in range(10):
    # input
    num = int(input())

    total += num

    if num not in num_dict:
        num_dict[num] = 1
    else: 
        num_dict[num] += 1

print(total // 10)

for i in num_dict:
    if num_dict[i] == max(num_dict.values()):
        print(i)
        break