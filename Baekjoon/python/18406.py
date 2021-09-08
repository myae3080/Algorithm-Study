# source : https://www.acmicpc.net/problem/18406
# string

# input
input_list = list(map(int, input()))

half = len(input_list) // 2
a, b = 0, 0

for i in range(len(input_list)):
    temp = input_list[i]

    if i < half:
        a += temp
    else:
        b += temp

print('LUCKY') if a == b else print('READY')