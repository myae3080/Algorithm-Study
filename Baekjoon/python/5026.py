# source : https://www.acmicpc.net/problem/5026
# string, parsing

for _ in range(int(input())):
    # input
    input_list = list(input().split('+'))

    if input_list[0] == 'P=NP':
        print('skipped')
    else:
        print(int(input_list[0]) + int(input_list[1]))