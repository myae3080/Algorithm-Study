# source : https://www.acmicpc.net/problem/2864
# math, greedy

# input
num1, num2 = input().split()

num_list1, num_list2 = list(num1), list(num2)
max_num, min_num = 0, 0

# max
for i in range(len(num_list1)):
    if num_list1[i] == "5":
        num_list1[i] = "6"

for i in range(len(num_list2)):
    if num_list2[i] == "5":
        num_list2[i] = "6"

max_num = int(''.join(num_list1)) + int(''.join(num_list2))

# min
for i in range(len(num_list1)):
    if num_list1[i] == "6":
        num_list1[i] = "5"

for i in range(len(num_list2)):
    if num_list2[i] == "6":
        num_list2[i] = "5"

min_num = int(''.join(num_list1)) + int(''.join(num_list2))

print(min_num, max_num)