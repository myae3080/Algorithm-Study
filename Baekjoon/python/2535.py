# sorting

# input
stu_list = sorted([list(map(int, input().split())) for _ in range(int(input()))], key=lambda stu: -stu[2])

print(' '.join(map(str, stu_list[0][:2])))
print(' '.join(map(str, stu_list[1][:2])))

if stu_list[0][0] == stu_list[1][0]:
    for stu in stu_list[2:]:
        if stu[0] != stu_list[0][0]:
            print(' '.join(map(str, stu[:2])))
            break
else:
    print(' '.join(map(str, stu_list[2][:2])))