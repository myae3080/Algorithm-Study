# string

# input
input_str = input()

[print(s) for s in [input_str[i:i + 10] for i in range(0, len(input_str), 10)]]