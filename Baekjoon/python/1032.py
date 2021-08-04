# source : https://www.acmicpc.net/problem/1032
# string

input_list = []

# input
[input_list.append(input()) for i in range(int(input()))]

pattern_list = list(input_list[0])
length = len(pattern_list)

for i in range(1, len(input_list)):
    temp = input_list[i]

    for j in range(length):
        if pattern_list[j] != temp[j]:
            pattern_list[j] = '?'

print(''.join(pattern_list))