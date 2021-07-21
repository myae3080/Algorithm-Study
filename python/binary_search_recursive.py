target_list = [14, 9, 8, 3, 1, 5, 7, 2, 4, 10, 13, 11, 6, 12]

# 정렬된 list를 param으로 넘겨야 함
def binary_search_recursive(target_list:list, start:int, end:int, target_val:int):
    mid = (start + end) // 2

    # 값을 찾을 수 없을 때 조건
    if mid > len(target_list) - 1 or start > end:
        return False

    if target_list[mid] > target_val:
        end = mid - 1
        return binary_search_recursive(target_list, start, end, target_val)
    elif target_list[mid] < target_val:
        start = mid + 1
        return binary_search_recursive(target_list, start, end, target_val)
    else:
        return True

print(binary_search_recursive(sorted(target_list), 0, len(target_list), 14))