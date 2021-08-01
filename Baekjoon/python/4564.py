# source : https://www.acmicpc.net/problem/4564

while True:
    result_list = []
    
    # input
    input_str = input()

    if input_str == '0':
        break

    result_list.append(input_str)

    while len(input_str) > 1:
        temp_num = 1

        for s in input_str:
            temp_num *= int(s)
        
        input_str = str(temp_num)
        result_list.append(input_str)
    
    print(' '.join(result_list))