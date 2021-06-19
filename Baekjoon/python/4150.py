# math, fibonacci

# input
input_num = int(input())

fibo_list = [0] * (input_num + 2)
fibo_list[1], fibo_list[2] = 1, 1

for i in range(3, input_num + 1):
    fibo_list[i] = fibo_list[i - 1] + fibo_list[i - 2]

print(fibo_list[input_num])