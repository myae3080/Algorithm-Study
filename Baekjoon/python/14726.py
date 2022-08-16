# source : https://www.acmicpc.net/problem/14726

for _ in range(int(input())):
    # input
    credit_card_num = input()

    total = 0
    for i in range(len(credit_card_num)):
        if i % 2 == 0:
            double = 2 * int(credit_card_num[i])

            if double >= 10:
                total += (1 + double % 10)
            else:
                total += double
        else:
            total += int(credit_card_num[i])

    print('T') if total % 10 == 0 else print('F')