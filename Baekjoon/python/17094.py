# source : https://www.acmicpc.net/problem/17094

# input
n = int(input())
string = input()

cnt_e = string.count('e')
cnt_2 = string.count('2')

print('e') if cnt_e > cnt_2 else print('yee') if cnt_e == cnt_2 else print('2')