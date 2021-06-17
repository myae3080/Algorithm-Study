# string

count = 0

for i in range(1, 9):
    # input
    for j, val in enumerate(list(input())):
        if i % 2 == 1:
            if (j + 1) % 2 == 1 and val == 'F':
                count += 1
        else:
            if (j + 1) % 2 == 0 and val == 'F':
                count += 1

print(count)