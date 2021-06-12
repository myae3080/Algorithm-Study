# remove duplicate

while True:
    # input
    input_list = list(map(int, input().split()))

    if input_list[0] == 0:
        break
    else:
        for i, n in enumerate(input_list[1:]):
            if i == 0:
                print(n, end=' ')

            if i != 0 and input_list[i] != n:
                print(n, end=' ')

        print('$')