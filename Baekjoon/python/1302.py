# data structure, string, sorting

import sys

# input
input = sys.stdin.readline

book_dict = {}
result_list = []

for _ in range(int(input())):
    # input
    book = input().rstrip()

    if book not in book_dict:
        book_dict[book] = 1
    else:
        book_dict[book] = book_dict[book] + 1

max_num = max(book_dict.values())

for k in book_dict.keys():
    if book_dict[k] == max_num:
        result_list.append(k)

result_list.sort()

print(result_list[0])