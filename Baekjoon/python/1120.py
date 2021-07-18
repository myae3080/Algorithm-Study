# string. brute forcing

# input
a_string, b_string = input().split()

min_num = 100
ab_range = len(b_string) - len(a_string) + 1

for i in range(ab_range):
    count = 0

    for j in range(len(a_string)):
        if a_string[j] != b_string[i + j]:
            count += 1

    min_num = min(min_num, count)

print(min_num)