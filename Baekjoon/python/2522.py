# star

# input
input_num = int(input())
line_num = (2 * input_num) - 1

half_num = round(line_num / 2) + 1 if input_num % 2 != 0 else round(line_num / 2)

for i in range(1, line_num + 1):
    if half_num > i:
        print((" " * (half_num - i)) + ("*" * i))
    elif half_num == i:
        print(("*" * i))
    else:
        print((" " * (i - half_num)) + ("*" * (line_num + 1 - i)))