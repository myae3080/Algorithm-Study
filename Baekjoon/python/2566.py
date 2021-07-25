db_list = []
max_val, row = 0, 0

for _ in range(9):
    # input
    temp_list = list(map(int, input().split()))
    max_val = max(max_val, max(temp_list))
    
    if temp_list.count(max_val):
        row = _ + 1

    db_list.append(temp_list)

print(max_val)
print(row, db_list[row - 1].index(max_val) + 1)