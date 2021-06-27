# string, octal number, binary number

# input
input_str = input()

octal_dict = {
    '000': '0',
    '001': '1',
    '010': '2',
    '011': '3',
    '100': '4',
    '101': '5',
    '110': '6',
    '111': '7',
}

length = len(input_str)
result = ''

if length % 3 == 2:
    input_str = '0' + input_str
elif length % 3 == 1:
    input_str = '00' + input_str

for i in range(0, len(input_str), 3):
    result += octal_dict[input_str[i:i + 3]]

print(result)