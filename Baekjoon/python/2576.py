# math

# input
odd_list = []

for i in range(7):
    input_num = int(input())

    if input_num % 2 == 1:
        odd_list.append(input_num)

if len(odd_list) == 0:
    print(-1)
else:
    print(sum(odd_list))
    print(min(odd_list))