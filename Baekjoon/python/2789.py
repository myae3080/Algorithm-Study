# string

# input
input_str = input()

inspection_str = 'CAMBRIDGE'

for s in inspection_str:
    if s in input_str:
        input_str = input_str.replace(s, '')

print(input_str)