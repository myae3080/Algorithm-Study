# source : https://www.acmicpc.net/problem/3460
# math

# input
t = int(input())

for _ in range(t):
    # input
    binary_list = list((bin(int(input()))[2:])[::-1])

    for i in range(len(binary_list)):
        if binary_list[i] == '1':
            print(i, end=' ')