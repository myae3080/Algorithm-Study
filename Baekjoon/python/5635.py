# sorting

import sys

# input
input = sys.stdin.readline

student_list = []

for i in range(int(input())):
    # input
    input_list = input().rstrip().split()

    temp_list = []
    temp_list.append(input_list[0])
    temp_list.append(int(input_list[1]))
    temp_list.append(int(input_list[2]))
    temp_list.append(int(input_list[3]))
    
    student_list.append(temp_list)

# sorting
student_list.sort(key=lambda stu: (stu[3], stu[2], stu[1]))

print(student_list[-1][0])
print(student_list[0][0])