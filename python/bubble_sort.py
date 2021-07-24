# bubble sorting

def bubble_sorting(target_list:list, desc:bool=False):
    length = len(target_list)

    for i in range(length):
        for j in range(0, length - i - 1):
            if not desc:
                if target_list[j + 1] < target_list[j]:
                    target_list[j], target_list[j + 1] = target_list[j + 1], target_list[j]
            else:
                if target_list[j + 1] > target_list[j]:
                    target_list[j], target_list[j + 1] = target_list[j + 1], target_list[j]

    return target_list

print(bubble_sorting([7, 4, 3, 6, 5, 1, 2]))
print(bubble_sorting([7, 4, 3, 6, 5, 1, 2], True))