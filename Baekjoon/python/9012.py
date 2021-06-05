# data structure, String, stack

# input
count = int(input())

result_list = []

for i in range(count):
    target_str = input()
    temp_num = 0

    for s in target_str:
        if s == "(":
            temp_num += 1
        else:
            temp_num -= 1
            
            if temp_num < 0:
                break

    if temp_num == 0:
        result_list.append("YES")
    else:
        result_list.append("NO")

for s in result_list:
    print(s)