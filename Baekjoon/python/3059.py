# source : https://www.acmicpc.net/problem/3059
# string

for _ in range(int(input())):
    alphabet = [0] * 26
    total = 0

    # input
    for c in input():
        alphabet[ord(c) - 65] += 1

    for i in range(26):
        if alphabet[i] == 0:
            total += (i + 65)

    print(total)