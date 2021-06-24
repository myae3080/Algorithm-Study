# string

while True:
    lower_count = 0
    upper_count = 0
    num_count = 0
    space_count = 0

    try:
        for c in input():
            char = ord(c)

            if char >= 97 and char <= 122:
                lower_count += 1
            elif char >= 65 and char <= 90:
                upper_count += 1
            elif char == 32:
                space_count += 1
            else:
                num_count += 1
        
        print(lower_count, upper_count, num_count, space_count)
    except EOFError:
        break