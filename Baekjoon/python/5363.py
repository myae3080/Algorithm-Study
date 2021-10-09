# source : https://www.acmicpc.net/problem/5363
# string

for _ in range(int(input())):
    # input
    input_list = list(input().split())

    print(' '.join(input_list[2:]) + ' ' + ' '.join(input_list[:2]))