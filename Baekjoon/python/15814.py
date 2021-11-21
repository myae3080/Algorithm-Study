# source : https://www.acmicpc.net/problem/15814
# string

input_str = list(input())

for _ in range(int(input())):
    # input
    i, j = map(int, input().split())
    
    input_str[i], input_str[j] = input_str[j], input_str[i]

print(''.join(input_str))