# source : https://www.acmicpc.net/problem/11365
# string

while True:
    # input
    input_str = input()

    if input_str == 'END':
        break

    input_list = list(input_str)
    print(''.join(input_list[::-1]))