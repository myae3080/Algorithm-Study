# string

while True:
    # input
    input_str = input()

    count = 0

    if input_str == '#':
        break

    for ch in set(input_str.lower()):
        aschi = ord(ch)

        if aschi >= 97 and aschi <= 122:
            count += 1

    print(count)