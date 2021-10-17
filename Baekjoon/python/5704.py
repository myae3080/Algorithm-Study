# source : https://www.acmicpc.net/problem/5704
# string

while True:
    # input
    input_str = input()
    alphabet = [0] * 26

    if input_str == '*':
        break

    for s in input_str:
        temp = ord(s) - 97

        if temp >= 0 and temp <= 26:
            alphabet[temp] += 1

    print('Y') if alphabet.count(0) == 0 else print('N')