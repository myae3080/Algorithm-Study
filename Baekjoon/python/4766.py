# source : https://www.acmicpc.net/problem/4766
# math

temperature_list, i = [], 0

while 1:
    # input
    temperature = float(input())

    if temperature == 999:
        break

    temperature_list.append(temperature)

    if len(temperature_list) > 1:
        print(format(temperature_list[i + 1] - temperature_list[i], ".2f"))
        i += 1