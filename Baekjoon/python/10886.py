# source : https://www.acmicpc.net/problem/10886
# math

num_dict = {}

for _ in range(int(input())):
    # input
    temp_num = int(input())

    if temp_num not in num_dict:
        num_dict[temp_num] = 0
    else:
        num_dict[temp_num] += 1

if len(num_dict) == 1:
    print('Junhee is cute!') if 1 in num_dict else print('Junhee is not cute!')
else:
    print('Junhee is cute!') if num_dict[1] > num_dict[0] else print('Junhee is not cute!')