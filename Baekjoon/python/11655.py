# string

result = ''

# input
for ch in input():
    ascii_code = ord(ch)

    # 대문자
    if ascii_code >= 65 and ascii_code <= 90:
        changed_code = ascii_code + 13

        if changed_code > 90:
            result += chr(changed_code - 26)
        else:
            result += chr(changed_code)
    # 소문자
    elif ascii_code >= 97 and ascii_code <= 122:
        changed_code = ascii_code + 13

        if changed_code > 122:
            result += chr(changed_code - 26)
        else:
            result += chr(changed_code)
    else:
        result += chr(ascii_code)

print(result)