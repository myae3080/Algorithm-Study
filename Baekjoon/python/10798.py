# string

# input
db_list = [list(input()) for i in range(5)]
length_list = [len(li) for li in db_list]

result = ''

for l in range(max(length_list)):
    for i in range(5):
        if l < len(db_list[i]):
            result += db_list[i][l]
        else:
            continue

print(result)