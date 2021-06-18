# math

def factorial(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * factorial(n - 1)

# input
input_num = str(factorial(int(input())))

count = 0

if len(input_num) == 1:
    print(0)
else:
    for i in range(len(input_num) - 1, 0, -1):
        if input_num[i] == '0':
            count += 1
        else:
            print(count)
            break