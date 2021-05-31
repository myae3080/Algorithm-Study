# one dimensional array

# input
case_num = int(input())
double_list = []

for i in range(case_num):
    double_list.append(list(map(int, input().split())))

for list in double_list:
    # input
    case_list = list
    student_num = case_list[0]
    sum = 0
    over_average_count = 0

    for index in range(1, len(case_list)):
        sum += case_list[index]

    average = sum / student_num

    for index in range(1, len(case_list)):
        if case_list[index] > average:
            over_average_count += 1

    print(format(round(over_average_count / student_num * 100, 3), ".3f") + "%")
