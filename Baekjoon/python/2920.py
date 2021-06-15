# input
input_list = list(map(int, input().split()))

print('ascending') if input_list == sorted(input_list) else print('descending') if input_list == sorted(input_list, reverse=True) else print('mixed')