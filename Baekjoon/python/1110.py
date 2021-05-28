input_num = int(input())

total_cycle_num = 0
temp_num = input_num

while True:
    if total_cycle_num != 0 and input_num == temp_num:
        break
    
    total_cycle_num += 1

    num_by_ten = temp_num // 10
    num_by_one = temp_num % 10

    temp_num = (num_by_one * 10) + ((num_by_ten + num_by_one) % 10) 

print(total_cycle_num)
    

