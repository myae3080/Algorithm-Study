# source : https://www.acmicpc.net/problem/1871

for _ in range(int(input())):
    # input
    string, number = input().split('-')

    base10, digit = 0, 0

    for i in range(len(string) - 1, -1, -1):
        base10 += (ord(string[i]) - 65) * (26 ** digit)
        digit += 1

    print('nice') if abs(base10 - int(number)) <= 100 else print('not nice')