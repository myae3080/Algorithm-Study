# string

for _ in range(int(input())):
    # input
    str_list = input().split()

    print(' '.join([s[::-1] for s in str_list]))