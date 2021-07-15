# data structure, sorting, binary search

import sys

# input
input = sys.stdin.readline

def binary_search(end=int, num=int, note1=list):
    start = 0

    while start <= end:
        mid = (start + end) // 2

        if note1_list[mid] == num:
            return 1
        elif note1_list[mid] > num:
            end = mid - 1
        else:
            start = mid + 1

    return 0
        

for _ in range(int(input())):
    # input
    n = int(input())
    note1_list = list(map(int, input().split()))
    m = int(input())
    note2_list = list(map(int, input().split()))

    note1_list.sort()
    end = n - 1

    for num in note2_list:
        # binary search
        print(binary_search(end, num, note1_list))