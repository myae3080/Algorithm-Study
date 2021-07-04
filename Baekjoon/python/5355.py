# string

for i in range(int(input())):
    # input
    input_list = input().split()

    if len(input_list) > 1:
        target = float(input_list[0])

        for c in input_list[1:]:
            if c == '@':
                target *= 3
            if c == '%':
                target += 5
            if c == '#':
                target -= 7

        print('%0.2f' %target)