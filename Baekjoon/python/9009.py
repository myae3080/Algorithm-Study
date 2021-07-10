# fibonacci, math, greedy algorithm

fibo_list = [0] * 46
fibo_list[1], fibo_list[2] = 1, 1

# fibonacci list setting
for i in range(3, 46):
    fibo_list[i] = fibo_list[i - 2] + fibo_list[i - 1]



for i in range(int(input())):
    # input
    input_num = int(input())

    result_list = []

    for i in range(45, 1, -1):
        if fibo_list[i] <= input_num:
            result_list.append(fibo_list[i])
            input_num -= fibo_list[i]

            if input_num == 0:
                break

    print(str(sorted(result_list)).replace('[', '').replace(']', '').replace(',', ''))