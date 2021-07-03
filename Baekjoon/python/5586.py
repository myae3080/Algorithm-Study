# string

# input
input_str = input()

joi_count = 0
ioi_count = 0

for i in range(len(input_str) - 2):
    temp_str = input_str[i:i+3]
    
    if temp_str == 'JOI':
        joi_count += 1
    
    if temp_str == 'IOI':
        ioi_count += 1

print(joi_count)
print(ioi_count)