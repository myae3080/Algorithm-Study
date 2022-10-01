# source : https://www.acmicpc.net/problem/15873

# input
ab = input()

if ab[1] == '0':
    print(int(ab[0]) * 10 + int(ab[2:]))
else:
    print(int(ab[0]) + int(ab[1:]))