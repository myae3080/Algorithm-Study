# source : https://www.acmicpc.net/problem/1159
# string

dict = {}
selected = []

for _ in range(int(input())):
    # input
    input_first_char = input()[0]

    if input_first_char in dict:
        dict[input_first_char] += 1
    else:
        dict[input_first_char] = 1

for k, v in dict.items():
    if v >= 5:
        selected.append(k)

print(''.join(sorted(selected))) if len(selected) > 0 else print('PREDAJA')