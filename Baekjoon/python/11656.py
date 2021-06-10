# string, sorting

# input
input_str = input()

str_list = []

for i in range(len(input_str)):
    str_list.append(input_str[i:])

for s in sorted(str_list):
    print(s)