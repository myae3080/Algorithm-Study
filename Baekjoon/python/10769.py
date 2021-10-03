# source : https://www.acmicpc.net/problem/10769
# string

# input
input_str = input()

happy = input_str.count(':-)')
sad = input_str.count(':-(')

if happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
else:
    if happy == 0 and sad == 0:
        print('none')
    else:
        print('unsure')