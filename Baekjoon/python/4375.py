# source : https://www.acmicpc.net/problem/4375

while True:
    try:
        # input
        n = int(input())
    except EOFError:
        break

    multiple = 0

    while True:
        multiple = multiple * 10 + 1
        if multiple % n == 0:
            print(len(str(multiple)))
            break