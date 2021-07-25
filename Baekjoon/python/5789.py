# string

for _ in range(int(input())):
    # input
    input_str = input()
    mid = len(input_str) // 2

    print('Do-it') if input_str[mid - 1] == input_str[mid] else print('Do-it-Not')