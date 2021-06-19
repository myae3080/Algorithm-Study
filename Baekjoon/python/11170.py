# brute force

zero_list = [0] * 1000001

for i in range(1000001):
    temp = str(i).count('0')

    if str(i).count('0') != 0:
        zero_list[i] = temp

for i in range(int(input())):
    from_num, to_num = map(int, input().split())

    print(sum(zero_list[from_num:to_num + 1]))