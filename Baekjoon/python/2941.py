# String

# input
input_str = input()

alphabet_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for alphabet in alphabet_list:
    if input_str.find(alphabet) != -1:
        input_str = input_str.replace(alphabet, '@')

print(len(input_str))