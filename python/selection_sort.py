# selection sorting

def selection_sort(target_list:list, desc:bool=False):
    for i in range(len(target_list) - 1):
        if not desc:
            min_value = min(target_list[i:])
            min_index = target_list[i:].index(min_value) + i

            target_list[i], target_list[min_index] = target_list[min_index], target_list[i]
        else:
            max_value = max(target_list[i:])
            max_index = target_list[i:].index(max_value) + i

            target_list[i], target_list[max_index] = target_list[max_index], target_list[i]
    return target_list

print(selection_sort([3, 5, 2, 4, 1, 3]))
print(selection_sort([3, 5, 2, 4, 1, 3], True))