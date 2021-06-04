# math : constructor

# input
num = int(input())

result_num = 0

for i in range(1, num + 1):
    ctor = i + sum(map(int, str(i)))

    if ctor == num:
        result_num = i
        break

print(result_num)