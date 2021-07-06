# string

result = ''

for ch in input():
    ascii_code = ord(ch)

    if ascii_code - 3 > 64:
        result += chr(ascii_code - 3)
    else:
        result += chr(ascii_code + 23)

print(result)