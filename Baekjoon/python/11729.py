# recursion

# input
round_count = int(input())

# tower
process_list = []

# a : from / b : temp / c : to
def hanoi(n, a, b, c):
    if n == 1:
        process_list.append(a + ' ' + c)
        return
    else:
        hanoi(n - 1, a, c, b)
        process_list.append(a + ' ' + c)
        hanoi(n - 1, b, a, c)

hanoi(round_count, '1', '2', '3')

print(len(process_list))

for str in process_list:
    print(str)