# String

# input
str_num1, str_num2 = input().split()
result_num = 0

result_num = max(int(str_num1[::-1]), int(str_num2[::-1]))

print(result_num)

