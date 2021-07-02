# math

total = 0
max_num = 0

for i in range(4):
    # input
    out_num, in_num = map(int, input().split())

    max_num = max(max_num, total, total - out_num + in_num)
    total = total - out_num + in_num

print(max_num)