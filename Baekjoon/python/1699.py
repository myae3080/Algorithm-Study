# math, dp

# input
num = int(input())

dp_list = [n for n in range(num + 1)]

for i in range(1, num + 1):
    for j in range(1, i):
        square = j * j

        if square > i:
            break
        else:
            if square == i:
                dp_list[i] = 1
            # dp_list[square] 배열 접근 시 시간초과로 1로 변경
            elif dp_list[i] > dp_list[i - square] + 1:
                dp_list[i] = dp_list[i - square] + 1

print(dp_list[num])