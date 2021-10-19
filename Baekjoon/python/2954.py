# source : https://www.acmicpc.net/problem/2954
# string

# input
input_list = list(input())

for i, s in enumerate(input_list):
    if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
        del input_list[i + 1]
        del input_list[i + 1]

print(''.join(input_list))