# multiples & divisors

while True:
    # input
    front_num, back_num = map(int, input().split())

    if front_num == 0 and back_num == 0:
        break
    
    if back_num % front_num == 0:
        print('factor')
    elif front_num % back_num == 0:
        print('multiple')
    else:
        print('neither')