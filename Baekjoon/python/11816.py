# math, string, parsing

# input
input_str = input()

if 'x' in input_str:
    print(int(input_str, 16))
elif input_str.startswith('0'):
    print(int(input_str, 8))
else:
    print(input_str)