# source : https://www.acmicpc.net/problem/11091
# string

for _ in range(int(input())):
    alphabet = [0] * 26

    # input
    for c in set(input()):
        target_num = ord(c.lower()) - 97

        if target_num >= 0 and target_num <= 26:
            alphabet[target_num] += 1

    if alphabet.count(0) == 0:
        print('pangram')
    else:
        print('missing', end=' ')
        for i in range(26):
            if alphabet[i] == 0:
                print(chr(i + 97), end='')
        
        print()