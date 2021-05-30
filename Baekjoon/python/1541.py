# greedy

# input
expression_list = input().split('-')

num_list = []
sum = 0

for i in range(len(expression_list)):
    temp_num = 0
    
    if i == 0:
        for str in expression_list[i].split('+'):
            temp_num += int(str)

        num_list.append(temp_num)
    else:
        for str in expression_list[i].split('+'):
            temp_num += int(str)

        num_list.append(-temp_num)

for num in num_list:
    sum += num

print(sum)