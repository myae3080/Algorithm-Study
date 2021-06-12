# math

# input
score_list = [int(input()) for n in range(6)]

apples = score_list[0] * 3 + score_list[1] * 2 + score_list[2]
bananas = score_list[3] * 3 + score_list[4] * 2 + score_list[5]

if apples > bananas:
    print('A')
elif apples == bananas:
    print('T')
else:
    print('B')