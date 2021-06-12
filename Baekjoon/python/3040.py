# brute force

# input
dwarf_list = [int(input()) for i in range(9)]
total = sum(dwarf_list)

for n in range(8):
    is_break = False

    for k in range(n + 1, 9):
        if total - dwarf_list[n] - dwarf_list[k] == 100:
            is_break = True
            del dwarf_list[k]
            del dwarf_list[n]

            break
    
    if is_break:
        break

[print(n) for n in dwarf_list]