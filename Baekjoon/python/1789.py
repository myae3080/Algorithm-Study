# greedy algorithm

# input
s = int(input())

result, num = 0, 0

while True:
    result += 1
    num += 1
    s -= num

    if s == 0:
        print(result)
        break
    # 음수가 되는 순간 직전의 개수가 최대값.
    elif s < 0:
        print(result - 1)
        break