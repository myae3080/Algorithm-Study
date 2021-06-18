# brute force

# input
dwarf_list = sorted([int(input()) for i in range(9)])
minus_num = sum(dwarf_list) - 100

for i in range(9):
    temp = dwarf_list[i]
    is_break = False

    for j in range(i + 1, 9):
        if temp + dwarf_list[j] == minus_num:
            dwarf_list.remove(dwarf_list[j])
            dwarf_list.remove(temp)
            is_break = True
            break

    if is_break:
        break

[print(n) for n in dwarf_list]