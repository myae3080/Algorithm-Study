# insertion sorting

def insertion_sort(target_list:list, desc:bool=False):
    for i in range(1, len(target_list)):
        while i > 0:
            if not desc:
                if target_list[i - 1] > target_list[i]:
                    target_list[i - 1], target_list[i] = target_list[i], target_list[i - 1]
            else:
                if target_list[i - 1] < target_list[i]:
                    target_list[i - 1], target_list[i] = target_list[i], target_list[i - 1]

            i -= 1
    
    return target_list

print(insertion_sort([5, 3, 2, 4, 1, 3]))
print(insertion_sort([5, 3, 2, 4, 1, 3], True))