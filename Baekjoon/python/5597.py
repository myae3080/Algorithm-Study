student_list = [False] * 31

for i in range(28):
    # input
    student_list[int(input())] = True

for i in range(1, 31):
    if student_list[i] == False:
        print(i)