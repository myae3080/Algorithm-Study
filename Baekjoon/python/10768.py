# source : https://www.acmicpc.net/problem/10768

# input
month, day = int(input()), int(input())

if month < 2:
    print('Before')
else:
    if month == 2:
        if day > 18:
            print('After')
        elif day < 18:
            print('Before')
        else:
            print('Special')
    else:
        print('After')