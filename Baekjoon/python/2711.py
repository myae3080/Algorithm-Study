# string

for _ in range(int(input())):
    # input
    idx, word = input().split()
    word_list = list(word)

    del word_list[int(idx) - 1]

    print(''.join(word_list))