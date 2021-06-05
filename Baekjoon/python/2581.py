# math, prime number

# input
first_num = int(input())
second_num = int(input())

sum = 0
min = 0
min_check = True

for num in range(first_num, second_num + 1):
    for i in range(2, num + 1):
        if num % i == 0:
            if i == num:
                sum += num
                if min_check:
                    min = num
                    min_check = False
            else:
                break

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)
