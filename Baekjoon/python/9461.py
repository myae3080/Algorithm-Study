# math, dp

n = 101
padovan_list = [0] * 101
padovan_list[1], padovan_list[2], padovan_list[3] = 1, 1, 1

for i in range(4, n):
    padovan_list[i] = padovan_list[i - 2] + padovan_list[i - 3]

for j in range(int(input())):
    # input
    print(padovan_list[int(input())])