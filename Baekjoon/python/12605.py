# data structure, string, stack

for i in range(int(input())):
    # input
    temp_list = input().split()

    print('Case #' + str(i + 1) + ':', end=' ')
    for i, s in enumerate(reversed(temp_list)):
        if i == len(temp_list) - 1:
            print(s)
        else:
            print(s, end=' ')